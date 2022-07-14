from django import forms
from django.core.validators import MaxLengthValidator

class IsmForm(forms.Form):
    ism = forms.CharField(max_length=40, required=True, strip=True, validators=[MaxLengthValidator(8)])
    fam = forms.CharField(max_length=40)
    ty = forms.IntegerField(min_value=1950, max_value=2022)