
from django.http import Http404
from django.shortcuts import render

import flights
from .models import Flight, Passenger
from django.http.response import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })
    
def flight(request, flight_id):
    try:
        flight = Flight.objects.get(pk=flight_id)
    
    except Flight.DoesNotExist:
        raise Http404("Flight not found.")
        
    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers": flight.passengers.all(),
        "no_passengers": Passenger.objects.exclude(flights=flight).all()
    })
    
def book(request, flight_id):
    
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)
        passenger = Passenger.objects.get(pk = int(request.POST["passenger"]))
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flights:flight", args=(flight.id,)))