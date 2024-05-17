from django.urls import path
from .views import student_application

urlpatterns = [
    path('', student_application, name='clarke_form'),
    # Add more URL patterns as needed
]
