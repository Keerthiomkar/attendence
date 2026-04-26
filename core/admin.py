from django.contrib import admin
from .models import CustomUser, Class, Section, Subject, Teacher, Student, Attendance, AttendanceRecord

# Register models for Django admin interface
admin.site.register(CustomUser)
admin.site.register(Class)
admin.site.register(Section)
admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Attendance)
admin.site.register(AttendanceRecord)
