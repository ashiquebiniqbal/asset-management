from datetime import timezone
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from psycopg2 import IntegrityError
from django.db import IntegrityError
from .models import Asset, Subscriber
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def shorten_url(request):
    # ...
    return HttpResponseRedirect()


def index(request):
    assets = Asset.objects.all()
    return render(request, "assets/index.html", {"assets": assets})


@login_required
def checkout(request, asset_id):
    asset = Asset.objects.get(id=asset_id)
    asset.checked_out_at = timezone.now()
    asset.save()
    return HttpResponseRedirect("/assets/")


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

