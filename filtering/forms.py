from django import forms
from .models import *

class ImgSaveForm(forms.ModelForm):
    class Meta:
        model = ImgSave
        fields = ["image"]