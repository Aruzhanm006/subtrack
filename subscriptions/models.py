from django.db import models
from django.contrib.auth.models import User

class Subscription(models.Model):
    SERVICE_CHOICES = [
        ('Netflix', 'Netflix'),
        ('Spotify', 'Spotify'),
        ('YouTube', 'YouTube Premium'),
        ('Other', 'Басқа'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service_name = models.CharField(max_length=100, choices=SERVICE_CHOICES)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    payment_date = models.DateField()
    reminder_days_before = models.IntegerField(default=1)  # ескерту күні

    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"{self.service_name} ({self.user.username})"
