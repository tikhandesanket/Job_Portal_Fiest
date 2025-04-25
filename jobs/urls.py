from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.job_list, name='job_list'),            # for applicants
    path('create/', views.job_create, name='job_create'),      # for recruiters
    # Add more if needed
]