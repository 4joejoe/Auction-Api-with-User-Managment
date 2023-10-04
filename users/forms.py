from django import forms
from .models import MyUser
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
  email = forms.EmailField()

  class Meta:
      model = MyUser
      fields = ['username', 'email','password','password2']