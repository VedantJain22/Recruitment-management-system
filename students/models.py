from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    enrollment = models.CharField(max_length=20, unique=True)
    contact = models.CharField(max_length=15)
    gender = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    tenth = models.CharField(max_length=4)
    twelfth = models.CharField(max_length=4)
    resume = models.FileField(upload_to='resumes/')
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    placement_history = models.TextField()

    def __str__(self):
        return self.user.username
