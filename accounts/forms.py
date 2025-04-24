from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Job

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    is_employer = forms.BooleanField(required=False, label="Register as Employer")

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description', 'salary', 'location', 'category', 'company']
