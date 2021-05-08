from django.shortcuts import render
from django.views import View


class PlaceView(View):
    def get(self, request):
        user = request.user
        content = {}

        show_welcome_toast = int(request.GET.get('welcome_toast', 0)) and user.is_authenticated
        if show_welcome_toast:
            user_name = f'{user.first_name} {user.last_name}'
            try:
                user_avatar = user.user_avatar.avatar.url
                content.update({
                    'user_name': user_name,
                    'user_avatar': user_avatar,
                    'show_welcome_toast': True,
                })
            except AttributeError:
                content.update({
                    'user_name': user_name,
                    'user_avatar': '',
                    'show_welcome_toast': True,
                })

        return render(request, 'place/place.html', content)
