from django.shortcuts import render
from django.views import View


class IndexView(View):
    def get(self, request):
        user = request.user
        content = {}
        if user.is_authenticated:
            user_name = f'{user.first_name} {user.last_name}'
            try:
                user_avatar = user.user_avatar.avatar.url
                content.update({
                    'user_name': user_name,
                    'user_avatar': user_avatar,
                })
            except AttributeError:
                content.update({
                    'user_name': user_name,
                    'user_avatar': '',
                })

        return render(request, 'index.html', content)
