from django.urls import path
from . import views

urlpatterns = [
    # Example route
    path('', views.job_list, name='job_list'),
]
