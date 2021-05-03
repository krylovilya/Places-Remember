from django.contrib.auth.models import User
from django.db import models


class UserAvatarModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_avatar')
    avatar = models.ImageField(upload_to='avatars')
    update_date = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'User avatar'
        verbose_name_plural = 'User avatars'
