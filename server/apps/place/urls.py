from apps.place.views import PlaceView, GetAllPlacesView, AddPlaceFormVIew, DeleteAndGenerateTestPlaces
from django.urls import path

urlpatterns = [
    path('', PlaceView.as_view()),
    path('get_all_places/', GetAllPlacesView.as_view()),
    path('add_place/', AddPlaceFormVIew.as_view()),
    path('delete_and_generate_test_places/', DeleteAndGenerateTestPlaces.as_view()),

]
