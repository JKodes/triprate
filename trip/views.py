from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Trip, Note
# Create your views here.
class HomeView(TemplateView):
    template_name = 'trip/index.html'

def trips_list(request):
    if request.user.is_authenticated:
        trips = Trip.objects.filter(owner=request.user)
    else:
        # Check if the user has visited the dashboard before
        if 'visited_dashboard' in request.session:
            # User has visited before, show the trips
            trips = Trip.objects.filter(owner=request.session['visited_dashboard'])
        else:
            # User has not visited before, show no trips
            trips = []

    context ={
        'trips' : trips
    }
    return render(request, 'trip/trip_list.html', context)