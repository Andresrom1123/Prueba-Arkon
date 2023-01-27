from rest_framework import serializers


from events.models import Event

class EventCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Event
		fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
	class Meta:
		model = Event
		fields = '__all__'
