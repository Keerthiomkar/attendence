"""
URL configuration for attendance_system project.
"""

from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# Temporary homepage (safe fallback)
def home(request):
    return HttpResponse("Django is working! 🚀")

urlpatterns = [
    # Admin panel
    path('admin/', admin.site.urls),

    # Main homepage (fallback)
    path('', home, name='home'),

    # App routes (core app)
    path('', include('core.urls')),
]
