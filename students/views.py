from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Student  # Ensure this import is correct
from django.shortcuts import render

def student_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('student_dashboard')
    return render(request, 'students/login.html')

def student_dashboard(request):
    if not request.user.is_authenticated:
        return redirect('student_login')
    student = Student.objects.get(user=request.user)
    return render(request, 'students/student_dashboard.html', {'student': student})

def profile(request):
    if not request.user.is_authenticated:
        return redirect('student_login')
    student = Student.objects.get(user=request.user)
    return render(request, 'students/profile.html', {'student': student})

def home(request):
    return render(request, 'home.html')
