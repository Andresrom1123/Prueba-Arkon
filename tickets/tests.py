from rest_framework.test import APITestCase

from events.models import Event
from tickets.models import Ticket


class TestTicketView(APITestCase):
	def setUp(self) -> None:
		self.url_base = 'http://localhost:8000/api/v1/'
		self.event_1 = Event.objects.create(name='event 1', max_tickets=3, start_at='2023-03-20', end_at='2023-04-10')
		self.ticket_1 = Ticket.objects.create(events=self.event_1, redeemed=True)


	def test_create_ticket(self):
		url = f'{self.url_base}tickets/'
		data = {
			"events": self.event_1.id
		}
		response = self.client.post(url, data=data)
		self.assertEqual(response.status_code, 201)


	def test_create_ticket_error(self):
		url = f'{self.url_base}tickets/{self.ticket_1.id}/'
		response = self.client.post(url)
		self.assertEqual(response.status_code, 400)


