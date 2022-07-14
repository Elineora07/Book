from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError


class RegistrationForm(forms.ModelForm):
    confirm = forms.CharField(max_length=128, widget=forms.PasswordInput, label="Parol takroran")
    
    def clean_confirm(self):
        if self.cleaned_data['confirm'] != self.cleaned_data['password']:
            raise ValidationError("Parollar bir xil emas")
    
        return self.cleaned_data['confirm']

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password']

        labels = {
            'first_name': "Ismingiz:",
            'email': "Email:",
            'password': "Parol"
        }
        widgets = {
           'password': forms.PasswordInput 
        }

class LoginForm(forms.Form):
    username = forms.CharField(max_length=128)
    password = forms.CharField(widget=forms.PasswordInput, min_length=6)