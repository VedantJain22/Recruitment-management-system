from django.urls import path
from .views import admin_dashboard, manage_students, manage_drives

urlpatterns = [
    path('dashboard/', admin_dashboard, name='admin_dashboard'),
    path('manage-students/', manage_students, name='manage_students'),
    path('manage-drives/', manage_drives, name='manage_drives'),
]
