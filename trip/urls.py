from django.urls import path

from .views import HomeView, TripCreateView, trips_list

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('dashboard/', trips_list, name='trip-list'),
    path('dashboard/trip/create', TripCreateView.as_view(), name='trip-create'),
    
]
