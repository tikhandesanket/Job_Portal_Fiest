from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        from .models import Profile  
        self.fields['user_type'] = forms.ChoiceField(
            choices=Profile.USER_TYPES,
            required=True
        )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
