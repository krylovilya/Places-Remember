from django.db import models
from django.contrib.auth.models import User


class PlaceModel(models.Model):
    title = models.CharField('Title', max_length=255)
    comment = models.TextField('Comment', max_length=1024)
    lat = models.DecimalField('Latitude', max_length=255, max_digits=9, decimal_places=6)
    lng = models.DecimalField('Longitude', max_length=255, max_digits=9, decimal_places=6)
    author = models.ForeignKey(User, verbose_name='Author', related_name='places', on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Place'
        verbose_name_plural = 'Places'
        ordering = ['-pub_date']

    def __str__(self):
        return self.title
