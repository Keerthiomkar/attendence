# Technology Stack

This document outlines all the programs, frameworks, and libraries used in this Student Attendance System project.

## 🚀 Backend Technologies
* **Python**: The core programming language used for the backend logic.
* **Django (>=5.2)**: The high-level Python web framework used to build the core application, handle routing, database models, and server-side rendering.
* **Django REST Framework**: Used for building Web APIs.
* **PostgreSQL (psycopg-binary)**: The relational database management system used for storing application data.
* **SQLite**: Used as the default local development database (`db.sqlite3`).
* **OpenPyXL**: A Python library used to read/write Excel 2010 xlsx/xlsm/xltx/xltm files.
* **ReportLab**: An open-source PDF generation library for Python, used for generating reports.
* **Pillow**: The Python Imaging Library, used for image processing functionalities.

## 🎨 Frontend Technologies
* **HTML5**: Used for structuring the web pages.
* **Tailwind CSS**: A utility-first CSS framework used for styling the application rapidly via CDN.
* **Vanilla JavaScript**: Used for client-side interactivity, DOM manipulation, and executing animations (e.g., auto-hiding messages).
* **CSS3**: Custom stylesheets (`style.css`) used for additional custom styling (like glassmorphism effects).

## 🛠️ UI Libraries & Assets
* **Font Awesome**: Used for comprehensive scalable vector icons across the application.
* **Animate.css**: A library of ready-to-use, cross-browser animations used for smooth page transitions and element animations.
* **Google Fonts**: Custom typography using the 'Inter' and 'Outfit' fonts.

## ⚙️ Deployment & Server Management
* **Gunicorn**: A Python WSGI HTTP Server for UNIX, used to serve the Django application in production.
* **Whitenoise**: Allows the web app to serve its own static files (CSS, JS, images) efficiently without relying on nginx/Apache.
* **Requests**: A simple HTTP library for Python used to send API requests over HTTP.
* **Django CORS Headers**: A Django App that adds Cross-Origin Resource Sharing (CORS) headers to responses, allowing in-browser requests to your Django application from other origins.
