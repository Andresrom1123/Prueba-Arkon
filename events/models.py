from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator



class Event(models.Model):
	name = models.CharField(max_length=300)
	max_tickets = models.IntegerField(validators=[
		MaxValueValidator(300),
		MinValueValidator(1)
	])
	start_at = models.DateField()
	end_at = models.DateField()

	def __str__(self):
		return self.name