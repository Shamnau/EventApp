from django.db import models

class Booking(models.Model):
    event = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateField()
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.event} - {self.name}"


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
