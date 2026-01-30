from django.test import TestCase
from .models import Booking

class BookingTest(TestCase):

    def test_create_booking(self):
        booking = Booking.objects.create(
            event="Tech Conference",
            name="Test User",
            email="test@example.com",
            date="2026-01-01",
            message="Looking forward"
        )
        self.assertEqual(booking.event, "Tech Conference")
