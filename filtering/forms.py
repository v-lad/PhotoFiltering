from django import forms
from .models import ImgSave


class ImgSaveForm(forms.ModelForm):
    class Meta:
        model = ImgSave
        fields = ["image"]
