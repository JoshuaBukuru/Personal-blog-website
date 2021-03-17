from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    #Inherits from the user creation form
    email = forms.EmailField()

    # nested namespace for configurations and keeps the configurations in one place
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    #Allows us to update username and email
    email = forms.EmailField()

    # nested namespace for configurations and keeps the configurations in one place
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    #Allows us to update image
    class Meta:
        model = Profile
        fields = ['image']

