# Student Attendance Management System

A complete full-stack web application for managing student attendance with role-based authentication, built with Django.

## Features

### Admin Features
- ✅ Dashboard with statistics (Total Classes, Subjects, Teachers, Students)
- ✅ Class Management (Create, View, Delete)
- ✅ Section Management (Add sections to classes)
- ✅ Subject Management (Create subjects for classes)
- ✅ Teacher Management (Create teachers, assign subjects and classes)
- ✅ Student Management (Add students to sections)

### Teacher Features
- ✅ Dashboard showing assigned classes and subjects
- ✅ Mark Attendance with interactive UI
  - Select Class, Section, Subject, and Date
  - All students default to **PRESENT (Green)**
  - Click any row to toggle to **ABSENT (Red)**
  - Click again to toggle back to **PRESENT (Green)**
  - Smooth visual feedback without page reload
  - Duplicate prevention for same date/class/subject

## Technology Stack

- **Backend**: Django 5.2.8
- **Database**: SQLite (default, PostgreSQL-compatible)
- **Frontend**: HTML, CSS, JavaScript
- **Styling**: Tailwind CSS (CDN)
- **Icons**: Font Awesome 6.4.0

## Project Structure

```
attendence/
├── attendance_system/          # Main project folder
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── core/                       # Main application
│   ├── models.py              # Database models
│   ├── views.py               # View functions
│   ├── forms.py               # Form definitions
│   ├── urls.py                # URL routing
│   ├── admin.py               # Admin configuration
│   ├── templates/             # HTML templates
│   │   ├── base.html
│   │   ├── login.html
│   │   ├── admin/
│   │   │   ├── dashboard.html
│   │   │   ├── manage_classes.html
│   │   │   ├── manage_subjects.html
│   │   │   ├── manage_teachers.html
│   │   │   └── manage_students.html
│   │   └── teacher/
│   │       ├── dashboard.html
│   │       └── mark_attendance.html
│   ├── static/
│   │   ├── css/style.css
│   │   └── js/attendance.js
│   └── management/
│       └── commands/
│           └── create_sample_data.py
└── manage.py
```

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Navigate to Project Directory
```bash
cd c:\Users\ravik\OneDrive\Desktop\attendence
```

### Step 2: Create Virtual Environment (Recommended)
```bash
python -m venv venv
```

### Step 3: Activate Virtual Environment
**Windows:**
```bash
venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### Step 4: Install Django
```bash
pip install django
```

### Step 5: Run Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 6: Create Sample Data
This will create:
- Admin user (admin / admin123)
- 2 Teachers (teacher1, teacher2 / teacher123)
- 3 Classes (BCA 1st, 2nd, 3rd Year)
- 2 Sections per class (Section A, Section B)
- Multiple subjects
- 10 students per section

```bash
python manage.py create_sample_data
```

### Step 7: Run Development Server
```bash
python manage.py runserver
```

### Step 8: Access the Application
Open your browser and navigate to:
```
http://127.0.0.1:8000/
```

## Default Login Credentials

### Admin Account
- **Username**: admin
- **Password**: admin123

### Teacher Accounts
- **Teacher 1**: teacher1 / teacher123
- **Teacher 2**: teacher2 / teacher123

## Usage Guide

### For Admin

1. **Login** with admin credentials
2. **Dashboard** shows statistics of classes, subjects, teachers, and students
3. **Manage Classes**: Create classes and add sections
4. **Manage Subjects**: Create subjects and assign to classes
5. **Manage Teachers**: 
   - Create teacher accounts
   - Assign subjects to teachers
   - Assign classes to teachers
6. **Manage Students**: Add students to sections

### For Teachers

1. **Login** with teacher credentials
2. **Dashboard** shows your assigned classes and subjects
3. **Mark Attendance**:
   - Select Class from your assigned classes
   - Select Section
   - Select Subject from your assigned subjects
   - Select Date (defaults to today)
   - Click "Show Students"
   - All students appear with **GREEN** background (Present)
   - **Click any row** to toggle to **RED** (Absent)
   - **Click again** to toggle back to **GREEN** (Present)
   - Click "Save Attendance" when done
   - System prevents duplicate attendance for same date/class/subject

## Database Models

- **CustomUser**: Extended user model with role (ADMIN/TEACHER)
- **Class**: Represents a class (e.g., BCA 1st Year)
- **Section**: Sections within a class (e.g., Section A)
- **Subject**: Subjects taught in classes
- **Teacher**: Teacher profile with assignments
- **Student**: Student information
- **Attendance**: Attendance session
- **AttendanceRecord**: Individual student attendance status

## Key Features Explained

### Interactive Attendance Toggle
- **Default State**: All students marked as PRESENT (green background)
- **Toggle Action**: Click/tap any student row
- **Visual Feedback**: 
  - PRESENT: Green background, check icon
  - ABSENT: Red background, X icon
- **No Page Reload**: JavaScript handles all interactions
- **Save**: AJAX request saves all attendance records

### Duplicate Prevention
- System checks if attendance already exists for:
  - Same Class
  - Same Section
  - Same Subject
  - Same Date
- Shows warning message if duplicate detected

### Role-Based Access Control
- **Admin**: Full access to all management features
- **Teacher**: Can only mark attendance for assigned classes/subjects
- Custom decorators enforce access control

## Troubleshooting

### Issue: "No module named 'core'"
**Solution**: Make sure you're in the correct directory and have run migrations

### Issue: "Table doesn't exist"
**Solution**: Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Issue: "Static files not loading"
**Solution**: Make sure STATICFILES_DIRS is configured in settings.py

### Issue: "Can't login"
**Solution**: Create sample data or create superuser manually:
```bash
python manage.py createsuperuser
```

## Creating Custom Superuser

If you want to create your own admin account:
```bash
python manage.py createsuperuser
```

Follow the prompts to enter username, email, and password.

## Production Deployment Notes

For production deployment:
1. Set `DEBUG = False` in settings.py
2. Configure `ALLOWED_HOSTS`
3. Use PostgreSQL instead of SQLite
4. Set up proper static file serving
5. Use environment variables for sensitive data
6. Enable HTTPS

## Support

For issues or questions, please refer to the Django documentation:
- https://docs.djangoproject.com/

## License

This project is created for educational purposes.

---

**Developed with Django 5.2.8 | 2026**
