from django.urls import path
from . import views

urlpatterns = [
    # Authentication
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # Admin URLs
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/classes/', views.manage_classes, name='manage_classes'),
    path('admin/subjects/', views.manage_subjects, name='manage_subjects'),
    path('admin/teachers/', views.manage_teachers, name='manage_teachers'),
    path('admin/allocations/', views.manage_allocations, name='manage_allocations'),
    path('admin/students/', views.manage_students, name='manage_students'),
    path('admin/students/export-excel/', views.export_students_excel, name='export_students_excel'),
    path('admin/students/export-pdf/', views.export_students_pdf, name='export_students_pdf'),
    path('admin/managers/', views.manage_managers, name='manage_managers'),
    
    # Teacher URLs
    path('teacher-dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('teacher/mark-attendance/', views.mark_attendance, name='mark_attendance'),
    path('teacher/export-attendance/', views.export_attendance, name='export_attendance'),
    path('teacher/save-attendance/', views.save_attendance, name='save_attendance'),
    
    # Manager URLs
    path('manager-dashboard/', views.manager_dashboard, name='manager_dashboard'),
    path('manager/save-remarks/', views.save_manager_remarks, name='save_manager_remarks'),
    path('manager/export-report/', views.export_manager_report_excel, name='export_manager_report_excel'),
    
    # Admin Attendance Report
    path('admin/attendance-report/', views.admin_attendance_report, name='admin_attendance_report'),
    path('admin/attendance/edit/', views.admin_edit_attendance, name='admin_edit_attendance'),
    path('admin/attendance/save/', views.admin_save_bulk_attendance, name='admin_save_bulk_attendance'),
    path('admin/attendance/add-session/', views.admin_add_attendance_session, name='admin_add_attendance_session'),

    # AJAX endpoints
    path('api/get-sections/', views.get_sections, name='get_sections'),
    path('api/get-sections-multiple/', views.get_sections_multiple, name='get_sections_multiple'),
    path('api/get-subjects/', views.get_subjects, name='get_subjects'),
    path('api/get-subjects-multiple/', views.get_subjects_multiple, name='get_subjects_multiple'),
    path('api/get-report-data/', views.api_get_report_data, name='api_get_report_data'),
]
