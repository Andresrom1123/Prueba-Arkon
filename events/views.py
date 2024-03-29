import datetime
from django.db.models import Q
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status

from events.models import Event
from tickets.models import Ticket
from events.serializers import EventRetrieveSerializer, EventCreateUpdateSerializer


class EventViewSet(viewsets.ModelViewSet):
	"""
	retrieve:
		Regresa un evento con el id.
	list:
		Regresa la lista de eventos.
	create:
		Crea un nuevo evento.
	update:
		Actualiza un evento.
	destroy:
		Borra un evento
	"""
	queryset = Event.objects.all()
	serializer_class = EventRetrieveSerializer

	def get_serializer_class(self):
		if self.action == "create" or self.action == "update":
			return EventCreateUpdateSerializer
		else:
			return EventRetrieveSerializer


	def destroy(self, request, pk=None):
		event = get_object_or_404(Event.objects.all(), pk=pk)
		tickets_event = Ticket.objects.filter(events__id=pk)

		end_at_day, now_day = event.end_at.strftime("%d"), datetime.datetime.now().strftime("%d")
		end_at_year, end_at_month = event.end_at.strftime("%Y"), event.end_at.strftime("%m")
		now_year, now_month = datetime.datetime.now().strftime("%Y"), datetime.datetime.now().strftime("%m")

		if (
			not end_at_year < now_year  or
			not end_at_day < now_day  and not end_at_month <= now_month
		):
			return Response({'error': 'You cannot delete an event if the end date has not yet passed'}, status=status.HTTP_400_BAD_REQUEST)

		if len(tickets_event) > 0:
			return Response({'error': 'You cannot delete a ticketed event'}, status=status.HTTP_400_BAD_REQUEST)

		event.delete()

		return Response(status=status.HTTP_204_NO_CONTENT)

	def retrieve(self, request, pk=None):
		event = get_object_or_404(Event.objects.all(), pk=pk)
		serializer = EventRetrieveSerializer(event)

		sell_tickets = Ticket.objects.filter(events__id=pk)
		redeemed_tickets = Ticket.objects.filter(Q(events__id=pk) & Q(redeemed=True))

		data = {
			'name': serializer.data['name'],
			'start_at': serializer.data['start_at'],
			'end_at': serializer.data['end_at'],
			"max_tickets": serializer.data['max_tickets'],
			'available_tickets': serializer.data['max_tickets'] - len(sell_tickets),
			'sell_tickets': len(sell_tickets),
			'redeemed_tickets': len(redeemed_tickets)
		}
		return Response(data)
