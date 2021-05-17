from apps.place.models import PlaceModel
from django.forms import ModelForm


class PlaceForm(ModelForm):
    class Meta:
        model = PlaceModel
        fields = ['title', 'comment', 'lat', 'lng']

    def __init__(self, user, *args, **kwargs):
        self.author_id = user.id
        super(PlaceForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        place = super(PlaceForm, self).save(commit=False)
        place.author_id = self.author_id
        if commit:
            place.save()
        return place
