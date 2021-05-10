from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.conf import settings


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
