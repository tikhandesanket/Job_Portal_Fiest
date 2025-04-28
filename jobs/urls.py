from django.urls import path
from . import views

urlpatterns = [
    path('job_list/', views.job_list, name='job_list'),         # for applicants
    path('create/', views.job_create, name='job_create'),
    path('jobs/<int:job_id>/apply/', views.job_apply, name='job_apply'), # for recruiters
    # Add more if needed
]