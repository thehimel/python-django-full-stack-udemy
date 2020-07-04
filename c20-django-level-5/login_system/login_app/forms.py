from django import forms
from django.contrib.auth.models import User
from login_app.models import UserProfileInfo


class UserForm(forms.ModelForm):
    # Editing the passworld filed for form input, else it will be CharField().
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_url', 'profile_pic')
