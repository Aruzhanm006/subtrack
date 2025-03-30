from django.shortcuts import render
from .models import Subscription


def index(request):
    return render(request, 'subscriptions/index.html')


def dashboard(request):
    if request.user.is_authenticated:
        subscriptions = Subscription.objects.filter(user=request.user)
        return render(request, 'subscriptions/dashboard.html', {'subscriptions': subscriptions})
    else:
        return render(request, 'subscriptions/unauthorized.html')