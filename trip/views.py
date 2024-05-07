from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DetailView

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


class TripCreateView(CreateView):
    model = Trip
    success_url = reverse_lazy('trip-list')
    fields = ['city', 'country', 'start_date', 'end_date']
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    
class TripDetailView(DetailView):
    model = Trip
    
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        trip = context['object']
        notes = trip.notes.all()
        context['notes'] = notes
        return context
    