from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404

from .serializers import TicketCreateSerializer
from .models import Ticket




class CreateTicketView(APIView):
	def post(self, request, format=None):
		serializer = TicketCreateSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RedeemedTicketView(APIView):
	def get_object(self, ticket_id):
		try:
			return Ticket.objects.get(id=ticket_id)
		except Ticket.DoesNotExist:
			raise Http404

	def post(self, request, ticket_id, format=None):
		ticket = self.get_object(ticket_id)

		if not ticket.redeemed:
			ticket.redeemed = True
			ticket.save()

			return Response({'success': 'Ticket has been redeemed'}, status=status.HTTP_200_OK)

		
		return Response({'error': 'The ticket has already been redeemed'}, status=status.HTTP_400_BAD_REQUEST)
