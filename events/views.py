from rest_framework import viewsets

from events.models import Event
from events.serializers import EventSerializer, EventCreateUpdateSerializer


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

	"""
	queryset = Event.objects.all()
	serializer_class = EventSerializer

	def get_serializer_class(self):
		if self.action == "create" or self.action == "update":
			return EventCreateUpdateSerializer
		else:
			return EventSerializer