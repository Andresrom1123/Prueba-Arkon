from django.urls import path, include
from rest_framework import routers

from events.views import EventViewSet
from tickets import views

router = routers.DefaultRouter()
router.register(r'events', EventViewSet)

urlpatterns = [
	path('', include(router.urls)),
	path('tickets', views.CreateTicketView.as_view()),
	path('tickets/<slug:ticket_id>', views.RedeemedTicketView.as_view()),
]
