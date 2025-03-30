from django.shortcuts import render, redirect
from .models import Subscription
from .forms import SubscriptionForm


def index(request):
    return render(request, 'subscriptions/index.html')


def dashboard(request):
    if request.user.is_authenticated:
        subscriptions = Subscription.objects.filter(user=request.user)
        return render(request, 'subscriptions/dashboard.html', {'subscriptions': subscriptions})
    else:
        return render(request, 'subscriptions/unauthorized.html')


def add_subscription(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            subscription = form.save(commit=False)
            subscription.user = request.user
            subscription.save()
            return redirect('dashboard')
    else:
        form = SubscriptionForm()
    
    return render(request, 'subscriptions/add_subscription.html', {'form': form})