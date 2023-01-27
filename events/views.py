from rest_framework import viewsets

from events.models import Event
from events.serializers import EventSerializer, EventCreateSerializer


class EventViewSet(viewsets.ModelViewSet):
	"""
	

	"""
	queryset = Event.objects.all()
	serializer_class = EventSerializer

	def get_serializer_class(self):
		if self.action == "create":
			return EventCreateSerializer
		else:
			return EventSerializer