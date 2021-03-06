from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
import random as random

class CustomUserCreationForm(UserCreationForm):
	class Meta(UserCreationForm):
		model = CustomUser
		fields = ('username', 'interests')

		
class CustomUserChangeForm(UserChangeForm):
	
	class Meta:
		model = CustomUser
		fields = ('username', 'interests')