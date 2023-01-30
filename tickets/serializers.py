from rest_framework import serializers

from tickets.models import Ticket



class CreateTicketSerializer(serializers.ModelSerializer):
	class Meta:
		model = Ticket
		fields = '__all__'
