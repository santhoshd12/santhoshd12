from django import forms
from . import models

class createpost(forms.ModelForm):
    class Meta:
        model = models.newtable
        fields = ['name','age','image']