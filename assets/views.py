from datetime import timezone
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from psycopg2 import IntegrityError
from django.db import IntegrityError
from .models import Asset, Subscriber
from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet
from .serializers import AssetSerializer
from . import payments



""" def home(request):
    return render(request, 'home.html') """
def home(request):
    assets = Asset.objects.all()
    return render(request, 'home.html', {'assets': assets})
    

def shorten_url(request):
    # ...
    return HttpResponseRedirect()


""" def index(request):
    assets = Asset.objects.all()
    return render(request, "assets/index.html", {"assets": assets})
from django.shortcuts import render, redirect """


def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        company = request.POST.get('company')
        employee = request.POST.get('employee')
        condition = request.POST.get('condition')
        asset = Asset(name=name, company=company, employee=employee, condition=condition)
        asset.save()
        return redirect('home')

    assets = Asset.objects.all()
    return render(request, 'assets/index.html', {'assets': assets})


def checkout(request):
    # Retrieve the amount and currency from the request data
    amount = request.POST.get('amount')
    currency = request.POST.get('currency')

    # Create a payment intent using the payments API
    client_secret = payments.create_payment_intent(amount, currency)

    # Pass the client secret to the template
    return render(request, 'checkout.html', {'client_secret': client_secret})

""" @login_required
def checkout(request, asset_id):
    asset = Asset.objects.get(id=asset_id)
    asset.checked_out_at = timezone.now()
    asset.save()
    return HttpResponseRedirect("/assets/")
 """

@login_required
def checkin(request, asset_id):
    asset = Asset.objects.get(id=asset_id)
    asset.checked_in_at = timezone.now()
    asset.save()
    return HttpResponseRedirect("/assets/")



def subscribe(request):
    if request.method == "POST":
        email = request.POST.get('email')

        try:
            # Create a new subscriber object
            subscriber = Subscriber.objects.create(email=email)
            # Redirect the user to the home page
            return redirect('home')
        except IntegrityError:
            error_message = "Email already subscribed."
            return render(request, 'home.html', {'error_message': error_message})

    return render(request, 'home.html')



class MyAPI(ModelViewSet):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer

