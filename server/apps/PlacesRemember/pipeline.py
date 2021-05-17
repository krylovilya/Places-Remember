import datetime
from io import BytesIO

import requests
from apps.PlacesRemember.models import UserAvatarModel
from django.core import files


def get_avatar(backend, strategy, details, response, user=None, *args, **kwargs):
    avatar_obj, created = UserAvatarModel.objects.get_or_create(user=user)
    updated_today = datetime.date.today() == avatar_obj.update_date
    if created or not updated_today:
        avatar_url = None
        if backend.name == 'vk-oauth2':
            avatar_url = response.get('photo', '')
        if backend.name == 'facebook':
            avatar_url = 'https://graph.facebook.com/{}/picture?type=small'.format(response['id'])
        avatar_response = requests.get(avatar_url)
        avatar_bytes = BytesIO()
        avatar_bytes.write(avatar_response.content)
        file_name = '{}.jpeg'.format(user.username)
        avatar_obj.avatar.save(file_name, files.File(avatar_bytes))
