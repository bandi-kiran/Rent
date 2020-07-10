from django.forms import forms

from Tolet.House.models import HouseInfo


class PostHouse(forms.ModelForm):
    class Meta:
        model = HouseInfo
        fields = '__all__'