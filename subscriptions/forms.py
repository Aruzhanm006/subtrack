from django import forms
from .models import Subscription

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['service_name', 'price', 'payment_date', 'reminder_days_before']
        widgets = {
            'payment_date': forms.DateInput(attrs={'type': 'date'}),
        }