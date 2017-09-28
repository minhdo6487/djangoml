from blog.models import User, Upload, User_Acc
from django import forms
from django.forms import CharField, Form, PasswordInput

class PostImage(forms.ModelForm):
    class Meta:
        model = Upload
        fields = [
            'pic'
        ]


class BlogUser(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        # model = User
        model = User_Acc
        fields = [
            'user_name',
            'password',
            'email',
            'age_date',
            'location'
        ]
