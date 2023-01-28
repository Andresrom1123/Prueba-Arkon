import datetime
from rest_framework import serializers


from events.models import Event
from tickets.models import Ticket

class EventCreateUpdateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Event
		fields = '__all__'

	def validate(self, data):
		start_at_day, end_at_day = data['start_at'].strftime("%d"), data['end_at'].strftime("%d")
		start_at_year, start_at_month = data['start_at'].strftime("%Y"), data['start_at'].strftime("%m")
		end_at_year, end_at_month = data['end_at'].strftime("%Y"), data['end_at'].strftime("%m")
		now_year, now_month = datetime.datetime.now().strftime("%Y"), datetime.datetime.now().strftime("%m")
		now_day = datetime.datetime.now().strftime("%d")

		if (
			start_at_year < now_year or
			start_at_month <= now_month and start_at_day < now_day
		):
			raise serializers.ValidationError("La fecha de inicio no debe ser menor a la de hoy")

		if (
			end_at_year < start_at_year or
			end_at_day < start_at_day and end_at_month <= now_month
		):
			raise serializers.ValidationError("La fecha de fin no debe ser menor a la de incio")


		return data

	def update(self, instance, validate_data):
		tickets_event = Ticket.objects.filter(events__id=instance.id)

		if (len(tickets_event) > validate_data.get('max_tickets')):
			raise serializers.ValidationError('La cantidad de tickets vendidos del evento no debe ser mayor al maximo de boletos')

		instance.name = validate_data.get('name', instance.name)
		instance.max_tickets = validate_data.get('max_tickets', instance.max_tickets)
		instance.start_at = validate_data.get('start_at', instance.start_at)
		instance.end_at = validate_data.get('end_at', instance.end_at)
		instance.save()
		return instance

class EventSerializer(serializers.ModelSerializer):
	class Meta:
		model = Event
		fields = '__all__'
