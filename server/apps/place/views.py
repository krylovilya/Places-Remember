from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.conf import settings
from apps.place.forms import PlaceForm
from apps.place.models import PlaceModel
import random


@method_decorator(login_required, name='dispatch')
class PlaceView(View):
    def get(self, request):
        user = request.user
        content = {
            'yandex_api': settings.YANDEX_API_KEY,
        }
        content.update(get_user_places(request, user))
        return render(request, 'place/place.html', content)


def get_user_places(request, user):
    places = user.places.all()
    paginator = Paginator(places, 15)
    page_number = request.GET.get('page', 1)
    page_object = paginator.get_page(page_number)
    return {'page_obj': page_object}


@method_decorator(login_required, name='dispatch')
class GetAllPlacesView(View):
    def get(self, request):
        user = request.user
        features = []
        for place in user.places.all():
            features.append({
                'type': 'Feature',
                'properties': {
                    'balloonContent': f'{place.title}<br>{place.comment}',
                },
                'geometry': {
                    'type': 'Point',
                    'coordinates': [place.lat, place.lng],
                }
            })
        response_dict = {
            'type': 'FeatureCollection',
            'features': features,
        }
        return JsonResponse(response_dict)


class AddPlaceFormVIew(View):
    def get(self, request):
        form = PlaceForm(request.user)
        return render(request, 'place/add_place.html', {
            'form': form,
            'yandex_api': settings.YANDEX_API_KEY,
        })

    def post(self, request):
        form = PlaceForm(request.user, request.POST)
        user = request.user
        if form.is_valid():
            form.cleaned_data.update({
                'author_id': user.id,
            })
            form.save()
            return HttpResponseRedirect('/place')
        else:
            return render(request, 'place/add_place.html', {
                'form': form,
                'yandex_api': settings.YANDEX_API_KEY,
            })


class DeleteAndGenerateTestPlaces(View):
    def get(self, request):
        request.user.places.all().delete()
        for i in range(50):
            tmp_object = PlaceModel()
            tmp_object.title = f"Test title {i}"
            tmp_object.comment = f"Test comment {i}"
            tmp_object.lat = random.uniform(55.997097, 56.019986)
            tmp_object.lng = random.uniform(92.771205, 92.965182)
            tmp_object.author_id = request.user.id
            tmp_object.save()
        return HttpResponseRedirect('/place')
