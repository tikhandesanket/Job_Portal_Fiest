from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    USER_TYPES = (
        ('recruiter', 'Recruiter'),
        ('applicant', 'Applicant'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='account_profile')
    user_type = models.CharField(max_length=20, choices=USER_TYPES)
