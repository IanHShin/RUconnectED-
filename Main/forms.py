from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout,authenticate 
from django.contrib.auth.models import User
from .models import Image, Text_Post
from django.forms import ModelForm
import numpy as np



class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length = 250,required= True)
    first_name = forms.CharField(max_length = 50, required = True)
    last_name = forms.CharField(max_length = 50, required = True)

    class Meta:
        model = User
        fields = ["first_name", "last_name","username","email", "password1", "password2"]


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = [ 'image']



