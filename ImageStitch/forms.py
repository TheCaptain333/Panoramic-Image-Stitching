from django import forms
from django.forms import ClearableFileInput
from .models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['Images']
        widgets = {
            
            'Images':ClearableFileInput(attrs={'multiple':True}),

        }
