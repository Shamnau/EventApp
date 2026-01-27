from django.contrib import admin
from .models import Booking
from .models import ContactMessage

admin.site.register(Booking)
admin.site.register(ContactMessage)