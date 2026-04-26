# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Install python dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . /app/

# Expose port (Render uses dynamic PORT)
EXPOSE 8000

# Run migrations + collectstatic + start server
CMD ["sh", "-c", "python manage.py showmigrations && python manage.py migrate --noinput && python manage.py collectstatic --noinput && gunicorn attendance_system.wsgi:application --bind 0.0.0.0:$PORT"]
