from django.urls import path
from . import views

urlpatterns = [
    path('job_list/', views.job_list, name='job_list'),         # for applicants
    path('job_create/', views.job_create, name='job_create'), 
    path('apply_job/<int:job_id>/', views.apply_job, name='apply_job'), # for applicants
    path('job_edit/<int:job_id>/', views.job_edit, name='job_edit'),# for recruiters
    path('job_delete/<int:job_id>/', views.job_delete, name='job_delete'),# for recruiters
    # Add more if needed
]