# Quick Setup Guide

## 🚀 Getting Started in 3 Minutes

### Step 1: Open Terminal
Navigate to the project directory:
```bash
cd c:\Users\ravik\OneDrive\Desktop\attendence
```

### Step 2: Run the Server
The database is already set up with sample data. Just run:
```bash
python manage.py runserver
```

### Step 3: Access the Application
Open your browser and go to:
```
http://127.0.0.1:8000/
```

## 🔑 Login Credentials

### Admin Account
- **Username**: `admin`
- **Password**: `admin123`

### Teacher Accounts
- **Teacher 1**: `teacher1` / `teacher123`
- **Teacher 2**: `teacher2` / `teacher123`

## ✨ Quick Test

### Test Admin Features
1. Login as admin
2. Go to "Manage Classes" → Create a new class
3. Go to "Manage Teachers" → View teacher assignments

### Test Teacher Features (IMPORTANT!)
1. Logout and login as `teacher1`
2. Click "Mark Attendance"
3. Select:
   - Class: **BCA 1st Year**
   - Section: **Section A**
   - Subject: **Python Programming**
   - Date: **Today**
4. Click "Show Students"
5. **Click any student row** → Watch it turn RED (Absent)
6. **Click again** → Watch it turn GREEN (Present)
7. Click "Save Attendance"

## 📊 Sample Data Included

- **3 Classes**: BCA 1st, 2nd, 3rd Year
- **6 Sections**: 2 per class
- **9 Subjects**: 3 per class
- **2 Teachers**: With assigned classes and subjects
- **60 Students**: 10 per section

## 📖 Full Documentation

See [README.md](file:///c:/Users/ravik/OneDrive/Desktop/attendence/README.md) for complete documentation.

---

**That's it! You're ready to go! 🎉**
