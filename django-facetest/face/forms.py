from face.models import Image, Number
from django import forms

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['name']
        labels = {'name': ''}

class NumberForm(forms.ModelForm):
    class Meta:
        model = Number
        fields = ['people_number']
        labels = {'people_number': ''}