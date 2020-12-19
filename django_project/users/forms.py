from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'special'})) # dodavanje klase kao widget
    last_name = forms.CharField(required=False, max_length=100)
    email = forms.EmailField() # required

    class Meta:
        model = User # model sa kojim forma interaguje
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(required=False, max_length=100) 
    last_name = forms.CharField(required=False, max_length=100)
    email = forms.EmailField()

    class Meta:
        model = User 
        fields = ['username', 'first_name', 'last_name', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']