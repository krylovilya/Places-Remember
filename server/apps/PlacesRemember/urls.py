from django.urls import path
from apps.PlacesRemember.views import IndexView

urlpatterns = [
    path('', IndexView.as_view()),

]
