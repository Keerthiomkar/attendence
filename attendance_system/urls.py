"""
URL configuration for attendance_system project.
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Admin panel
    path('admin/', admin.site.urls),

    # App routes (core app)
    path('', include('core.urls')),
]
