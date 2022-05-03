from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class CustomRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=254, widget=forms.TextInput({'placeholder': 'Username'}))
    email = forms.EmailField(widget=forms.EmailInput({'placeholder': 'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput({'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput({'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']