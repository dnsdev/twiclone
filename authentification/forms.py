__author__ = 'David'

from django import forms
from django.contrib.auth import authenticate


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput())

    def check_password(self):
        return authenticate(username=self.cleaned_data['username'],
                            password=self.cleaned_data['password'])