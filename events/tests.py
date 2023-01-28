from rest_framework.test import APITestCase

from events.models import Event
from tickets.models import Ticket


class TestEventViewSet(APITestCase):
	def setUp(self) -> None:
		self.url_base = 'http://localhost:8000/api/v1/'
		self.event_1 = Event.objects.create(name='event 1', max_tickets=3, start_at='2023-03-20', end_at='2023-04-10')
		self.ticket_1 = Ticket.objects.create(events=self.event_1)
		self.ticket_2 = Ticket.objects.create(events=self.event_1)

	def test_create_event_error(self):
		url = f'{self.url_base}events/'
		data = {
			'name': 'event 1',
			'max_tickets': 300,
			'start_at': '2023-01-27',
			'end_at': '2023-01-28'
		}
		response = self.client.post(url, data=data)
		# print(response.data)
		self.assertEqual(response.status_code, 400)


	def test_update_event_error(self):
		url = f'{self.url_base}events/{self.event_1.id}/'
		data = {
			'name': 'event 2',
			'max_tickets': 1,
			'start_at': '2023-01-29',
			'end_at': '2023-01-30'
		}
		response = self.client.put(url, data=data)
		print(response.data)
		self.assertEqual(response.status_code, 400)
