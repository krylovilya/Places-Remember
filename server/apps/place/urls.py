from django.urls import path
from apps.place.views import PlaceView, GetAllPlacesView

urlpatterns = [
    path('', PlaceView.as_view()),
    path('get_all_places/', GetAllPlacesView.as_view()),

]
