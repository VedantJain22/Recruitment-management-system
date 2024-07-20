from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', include('students.urls')),
    path('admins/', include('admins.urls')),
    path('', include('home.urls')),  # Include the home view in the root URL
]
