from blog.models import User, Upload
from django import forms
from django.forms import CharField, Form, PasswordInput

class PostImage(forms.ModelForm):
    class Meta:
        model = Upload
        fields = [
            'pic',
        ]




class BlogUser(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'email'
        ]
