from django.shortcuts import render, redirect
from .models import PlacementDrive  # Ensure this import is correct

def admin_dashboard(request):
    return render(request, 'admins/admin_dashboard.html')

def manage_students(request):
    return render(request, 'admins/manage_students.html')

def manage_drives(request):
    drives = PlacementDrive.objects.all()
    return render(request, 'admins/manage_drives.html', {'drives': drives})
