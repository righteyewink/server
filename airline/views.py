from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from airline.models import Flight, Passenger

# Create your views here.

def index(request):
    flights = Flight.objects.all()
    return render(request, 'airline/index.html', {
        'flights': flights    
    })

def flight(request, flight_id):
    # get the flight
    flight = Flight.objects.get(pk=flight_id)
    passengers = flight.passengers.all()
    non_passengers = Passenger.objects.exclude(flights=flight)
    return render(request, 'airline/flight.html', {
        'flight': flight,
        'passengers': passengers,
        'non_passengers': non_passengers
    })

def book(request, flight_id):
    if request.method == 'POST':
        # get the flight
        flight = Flight.objects.get(pk=flight_id)
        # get the passenger_id
        passenger_id = int(request.POST['passenger'])
        # get the select passenger
        passenger = Passenger.objects.get(pk=passenger_id)
        # add passenger to the flight
        passenger.flights.add(flight)
        # redirect user to flight page
        return HttpResponseRedirect(reverse('airline:flight', args=(flight_id, )))

def unbook(request, flight_id):
    if request.method == 'POST':
        # get the flight
        flight = Flight.objects.get(pk=flight_id)
        # get the passenger_id
        passenger_id = int(request.POST['passenger'])
        # get the select passenger
        passenger = Passenger.objects.get(pk=passenger_id)
        # remove passenger from the flight
        passenger.flights.remove(flight)
        # redirect user to flight page
        return HttpResponseRedirect(reverse('airline:flight', args=(flight_id, )))
