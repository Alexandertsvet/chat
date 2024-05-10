from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import UserChat

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = UserChat
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = UserChat
        fields = ('username', 'email')