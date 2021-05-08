from django.urls import path
from apps.place.views import PlaceView

urlpatterns = [
    path('', PlaceView.as_view()),

]
