from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    salary = models.IntegerField()
    location = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)

class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    cover_letter = models.TextField()
    applied_at = models.DateTimeField(auto_now_add=True)

class Profile(models.Model):
    USER_TYPES = (
        ('recruiter', 'Recruiter'),
        ('applicant', 'Applicant'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=20, choices=USER_TYPES)

    def __str__(self):
        return f"{self.user.username} - {self.user_type}"