from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


# Remove the import of Profile at the top to avoid circular import
# from .models import Profile

class RegisterForm(forms.ModelForm):
    user_type = forms.ChoiceField(choices=[('applicant', 'Employer'), ('recruiter', 'Job Seeker')])

    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        if commit:
            user.save()
        # Lazy import Profile here to avoid circular import
        from .models import Profile
        Profile.objects.create(
            user=user,
            user_type=self.cleaned_data.get('user_type')
        )
        return user

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())
