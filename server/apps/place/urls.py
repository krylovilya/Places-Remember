from django.urls import path
from apps.place.views import PlaceView, GetAllPlacesView, AddPlaceFormVIew

urlpatterns = [
    path('', PlaceView.as_view()),
    path('get_all_places/', GetAllPlacesView.as_view()),
    path('add_place/', AddPlaceFormVIew.as_view()),

]
