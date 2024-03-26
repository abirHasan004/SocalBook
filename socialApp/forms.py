from django import forms
from .models import *


class Forms(forms.ModelForm):
    
    class Meta:
        model =POST
        fields='__all__'
