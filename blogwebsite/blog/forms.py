from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Blogger

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email ID")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Blogger
        fields = ['profile_pic']

class AboutUpadateForm(forms.ModelForm):

    class Meta:
        model = Blogger
        fields = ['about']