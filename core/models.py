from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError

class CustomUser(AbstractUser):
    """Custom user model with role-based authentication"""
    ROLE_CHOICES = [
        ('ADMIN', 'Admin'),
        ('TEACHER', 'Teacher'),
        ('MANAGER', 'Manager'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='TEACHER')

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"


class Class(models.Model):
    """Represents a class/course (e.g., BCA 1st Year)"""
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Classes"
        ordering = ['name']

    def __str__(self):
        return self.name


class Section(models.Model):
    """Represents a section within a class (e.g., Section A)"""
    class_ref = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='sections')
    name = models.CharField(max_length=50)

    class Meta:
        unique_together = ['class_ref', 'name']
        ordering = ['class_ref', 'name']

    def __str__(self):
        return f"{self.class_ref.name} - {self.name}"


class Subject(models.Model):
    """Represents a subject taught in a class"""
    name = models.CharField(max_length=100)
    class_ref = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='subjects')
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='subjects', null=True, blank=True)
    code = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        unique_together = ['name', 'class_ref']
        ordering = ['class_ref', 'name']

    def __str__(self):
        return f"{self.name} ({self.class_ref.name})"


class Teacher(models.Model):
    """Represents a teacher with assigned subjects and classes"""
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='teacher_profile')
    employee_id = models.CharField(max_length=50, unique=True)
    password_text = models.CharField(max_length=128, blank=True, null=True, help_text="Plain text password for admin reference (Security Risk)")
    phone = models.CharField(max_length=15, blank=True, null=True)
    assigned_subjects = models.ManyToManyField(Subject, related_name='teachers', blank=True)
    assigned_classes = models.ManyToManyField(Class, related_name='teachers', blank=True)
    assigned_sections = models.ManyToManyField(Section, related_name='teachers', blank=True)

    def __str__(self):
        return f"{self.user.get_full_name() or self.user.username} ({self.employee_id})"


class Student(models.Model):
    """Represents a student in a section"""
    roll_number = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='students')
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        ordering = ['roll_number']

    def __str__(self):
        return f"{self.roll_number} - {self.name}"


class Attendance(models.Model):
    """Represents an attendance session for a specific class, section, subject, and date"""
    class_ref = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='attendances')
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='attendances')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='attendances')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='attendances')
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['class_ref', 'section', 'subject', 'date']
        ordering = ['-date', '-created_at']

    def __str__(self):
        return f"{self.section} - {self.subject.name} - {self.date}"

    def clean(self):
        """Validate that section belongs to the class"""
        if self.section and self.class_ref and self.section.class_ref != self.class_ref:
            raise ValidationError("Section does not belong to the selected class.")


class AttendanceRecord(models.Model):
    """Represents individual student attendance status"""
    STATUS_CHOICES = [
        ('PRESENT', 'Present'),
        ('ABSENT', 'Absent'),
    ]
    attendance = models.ForeignKey(Attendance, on_delete=models.CASCADE, related_name='records')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendance_records')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PRESENT')
    manager_remarks = models.TextField(blank=True, null=True, help_text="Notes added by a manager for absent students")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['attendance', 'student']
        ordering = ['student__roll_number']

    def __str__(self):
        return f"{self.student.name} - {self.status}"
