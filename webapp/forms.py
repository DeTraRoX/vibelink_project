from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    gender = forms.CharField(required=True)
    interest = forms.CharField(required=True)
    month = forms.CharField(required=True)
    day = forms.CharField(required=True)
    year = forms.CharField(required=True)
    avatar = forms.ImageField(required=False)

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your name',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email',
                'required': True
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write your message here...',
                'required': True,
                'rows': 5,
            }),
        }
