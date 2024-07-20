# students/urls.py
from django.urls import path
from .views import student_login, student_dashboard, profile

urlpatterns = [
    path('login/', student_login, name='student_login'),
    path('dashboard/', student_dashboard, name='student_dashboard'),
    path('profile/', profile, name='profile'),
]
