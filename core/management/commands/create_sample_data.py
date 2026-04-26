from django.core.management.base import BaseCommand
from core.models import CustomUser, Class, Section, Subject, Teacher, Student


class Command(BaseCommand):
    help = 'Creates sample data for testing the attendance system'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Creating sample data...'))
        
        # Create admin user if not exists
        if not CustomUser.objects.filter(username='admin').exists():
            admin = CustomUser.objects.create_superuser(
                username='admin',
                password='admin123',
                email='admin@example.com',
                first_name='Admin',
                last_name='User',
                role='ADMIN'
            )
            self.stdout.write(self.style.SUCCESS('[OK] Created admin user: admin / admin123'))
        else:
            self.stdout.write(self.style.WARNING('Admin user already exists'))
        
        # Create classes
        classes_data = [
            'BCA 1st Year',
            'BCA 2nd Year',
            'BCA 3rd Year',
        ]
        
        classes = {}
        for class_name in classes_data:
            class_obj, created = Class.objects.get_or_create(name=class_name)
            classes[class_name] = class_obj
            if created:
                self.stdout.write(self.style.SUCCESS(f'[OK] Created class: {class_name}'))
        
        # Create sections
        sections_data = ['Section A', 'Section B']
        sections = {}
        
        for class_name, class_obj in classes.items():
            for section_name in sections_data:
                section, created = Section.objects.get_or_create(
                    class_ref=class_obj,
                    name=section_name
                )
                sections[f'{class_name} - {section_name}'] = section
                if created:
                    self.stdout.write(self.style.SUCCESS(f'[OK] Created section: {class_name} - {section_name}'))
        
        # Create subjects
        subjects_data = {
            'BCA 1st Year': [
                ('Python Programming', 'CS101'),
                ('Database Management', 'CS102'),
                ('Web Development', 'CS103'),
            ],
            'BCA 2nd Year': [
                ('Java Programming', 'CS201'),
                ('Data Structures', 'CS202'),
                ('Operating Systems', 'CS203'),
            ],
            'BCA 3rd Year': [
                ('Software Engineering', 'CS301'),
                ('Machine Learning', 'CS302'),
                ('Cloud Computing', 'CS303'),
            ],
        }
        
        subjects = {}
        for class_name, subject_list in subjects_data.items():
            class_obj = classes[class_name]
            for subject_name, subject_code in subject_list:
                subject, created = Subject.objects.get_or_create(
                    name=subject_name,
                    class_ref=class_obj,
                    defaults={'code': subject_code}
                )
                subjects[f'{class_name} - {subject_name}'] = subject
                if created:
                    self.stdout.write(self.style.SUCCESS(f'[OK] Created subject: {subject_name} ({subject_code})'))
        
        # Create teachers
        teachers_data = [
            {
                'username': 'teacher1',
                'password': 'teacher123',
                'first_name': 'John',
                'last_name': 'Doe',
                'employee_id': 'T001',
                'phone': '9876543210',
                'assigned_classes': ['BCA 1st Year', 'BCA 2nd Year'],
                'assigned_subjects': ['BCA 1st Year - Python Programming', 'BCA 1st Year - Database Management'],
            },
            {
                'username': 'teacher2',
                'password': 'teacher123',
                'first_name': 'Jane',
                'last_name': 'Smith',
                'employee_id': 'T002',
                'phone': '9876543211',
                'assigned_classes': ['BCA 2nd Year', 'BCA 3rd Year'],
                'assigned_subjects': ['BCA 2nd Year - Java Programming', 'BCA 2nd Year - Data Structures'],
            },
        ]
        
        for teacher_data in teachers_data:
            if not CustomUser.objects.filter(username=teacher_data['username']).exists():
                user = CustomUser.objects.create_user(
                    username=teacher_data['username'],
                    password=teacher_data['password'],
                    first_name=teacher_data['first_name'],
                    last_name=teacher_data['last_name'],
                    role='TEACHER'
                )
                
                teacher = Teacher.objects.create(
                    user=user,
                    employee_id=teacher_data['employee_id'],
                    phone=teacher_data['phone']
                )
                
                # Assign classes
                for class_name in teacher_data['assigned_classes']:
                    teacher.assigned_classes.add(classes[class_name])
                
                # Assign subjects
                for subject_key in teacher_data['assigned_subjects']:
                    teacher.assigned_subjects.add(subjects[subject_key])
                
                self.stdout.write(self.style.SUCCESS(
                    f'[OK] Created teacher: {teacher_data["first_name"]} {teacher_data["last_name"]} '
                    f'({teacher_data["username"]} / {teacher_data["password"]})'
                ))
            else:
                self.stdout.write(self.style.WARNING(f'Teacher {teacher_data["username"]} already exists'))
        
        # Create students
        student_count = 0
        for section_key, section in sections.items():
            # Create 10 students per section
            for i in range(1, 11):
                roll_number = f'{section.class_ref.name[:3].upper()}{section.name[-1]}{i:02d}'
                
                if not Student.objects.filter(roll_number=roll_number).exists():
                    Student.objects.create(
                        roll_number=roll_number,
                        name=f'Student {roll_number}',
                        section=section,
                        email=f'{roll_number.lower()}@example.com',
                        phone=f'98765432{i:02d}'
                    )
                    student_count += 1
        
        if student_count > 0:
            self.stdout.write(self.style.SUCCESS(f'[OK] Created {student_count} students'))
        
        self.stdout.write(self.style.SUCCESS('\n' + '='*50))
        self.stdout.write(self.style.SUCCESS('Sample data created successfully!'))
        self.stdout.write(self.style.SUCCESS('='*50))
        self.stdout.write(self.style.SUCCESS('\nLogin Credentials:'))
        self.stdout.write(self.style.SUCCESS('Admin: admin / admin123'))
        self.stdout.write(self.style.SUCCESS('Teacher 1: teacher1 / teacher123'))
        self.stdout.write(self.style.SUCCESS('Teacher 2: teacher2 / teacher123'))
        self.stdout.write(self.style.SUCCESS('='*50))

