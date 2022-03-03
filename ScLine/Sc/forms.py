from pyexpat import model
from attr import fields
from django import forms
from .models import ScLineUsr

class ScLineUsrForm(forms.ModelForm):
    class Meta:
        model = ScLineUsr
        fields = ('username', 'vk', 'inst', 'tiktok', 'youtube',
                   'facebook', 'link1', 'link2', 'link3', 'link4',
                   'link5',)
