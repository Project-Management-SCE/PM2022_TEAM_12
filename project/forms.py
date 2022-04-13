from django import forms
from .models import Driver

class MyfileuploadForm(forms.Form):
    filename=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

