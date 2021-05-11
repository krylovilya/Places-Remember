from apps.place.models import PlaceModel
from django.contrib.auth.models import User
from django.test import Client
from django.test import TestCase


class PlaceTestClass(TestCase):
    def setUp(self):
        self.user = User.objects.create(first_name='Big', last_name='Bob')
        self.client = Client()
        self.client.force_login(self.user)
        self.client.get('/place/delete_and_generate_test_places/')

    def test_add_place(self):
        response = self.client.post("/place/add_place/", data={
            'title': 'Test title',
            'comment': 'Test comment',
            'lat': 0.0,
            'lng': 0.0,
            'author_id': self.user.id
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response["Location"], "/place")

    def test_place_list_view(self):
        response = self.client.get('/place/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(PlaceModel.objects.count(), 50)
        self.assertEqual(response.context['page_obj'].paginator.count, 50)
        self.assertTemplateUsed(response, 'place/place.html')
