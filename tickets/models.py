from django.db import models
from django.utils import timezone

from events.models import Event



class Ticket(models.Model):
	events = models.ForeignKey(Event, related_name='events_tickets', on_delete=models.CASCADE)
	redeemed = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_created=timezone.now, auto_now_add=True)

	class Meta:
		ordering = ['-created_at']
