from django import forms
from django.contrib.auth.forms import UserCreationForm
from datetime import date
from .models import CustomUser, Class, Section, Subject, Teacher, Student


class LoginForm(forms.Form):
    """Form for user login"""
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-blue-500 focus:border-transparent',
            'placeholder': 'Username'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-4 py-3 pr-10 rounded-lg border border-gray-300 focus:ring-2 focus:ring-blue-500 focus:border-transparent',
            'placeholder': 'Password'
        })
    )


class ClassForm(forms.ModelForm):
    """Form for creating/editing classes"""
    class Meta:
        model = Class
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-blue-500',
                'placeholder': 'e.g., BCA 1st Year'
            })
        }


class SectionForm(forms.ModelForm):
    """Form for creating/editing sections"""
    class Meta:
        model = Section
        fields = ['class_ref', 'name']
        widgets = {
            'class_ref': forms.Select(attrs={
                'class': 'w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-blue-500'
            }),
            'name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-blue-500',
                'placeholder': 'e.g., Section A'
            })
        }


class SubjectForm(forms.ModelForm):
    """Form for creating/editing subjects"""
    class Meta:
        model = Subject
        fields = ['name', 'class_ref', 'section', 'code']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-blue-500',
                'placeholder': 'e.g., Python Programming'
            }),
            'class_ref': forms.Select(attrs={
                'class': 'w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-blue-500',
                'id': 'id_subject_class_ref'
            }),
            'section': forms.Select(attrs={
                'class': 'w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-blue-500',
                'id': 'id_subject_section'
            }),
            'code': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-blue-500',
                'placeholder': 'e.g., CS101 (optional)'
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Initially empty queryset for section, or populate if data exists
        self.fields['section'].queryset = Section.objects.none()
        
        if 'class_ref' in self.data:
            try:
                class_id = int(self.data.get('class_ref'))
                self.fields['section'].queryset = Section.objects.filter(class_ref_id=class_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk and self.instance.section:
            self.fields['section'].queryset = self.instance.class_ref.sections.order_by('name')


class TeacherCreationForm(UserCreationForm):
    """Form for creating teachers with user accounts"""
    first_name = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-blue-500',
            'placeholder': 'First Name'
        })
    )
    last_name = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Last Name'
        })
    )
    employee_id = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Employee ID'
        })
    )
    phone = forms.CharField(
        max_length=15,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Phone Number (optional)'
        })
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Username'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({
            'class': 'w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Password'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Confirm Password'
        })


class ManagerCreationForm(UserCreationForm):
    """Form for creating managers with user accounts"""
    first_name = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-blue-500',
            'placeholder': 'First Name'
        })
    )
    last_name = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Last Name'
        })
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Username'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({
            'class': 'w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Password'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Confirm Password'
        })


class TeacherAssignmentForm(forms.ModelForm):
    """Form for assigning subjects and classes to teachers"""
    class Meta:
        model = Teacher
        fields = ['assigned_subjects', 'assigned_classes']
        widgets = {
            'assigned_subjects': forms.CheckboxSelectMultiple(),
            'assigned_classes': forms.CheckboxSelectMultiple(),
        }

class TeacherAllocationForm(forms.Form):
    """Form for selecting a teacher and assigning classes/subjects"""
    teacher = forms.ModelChoiceField(
        queryset=Teacher.objects.all(),
        label="Select Teacher",
        widget=forms.Select(attrs={
            'class': 'w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-blue-500'
        })
    )
    assigned_classes = forms.ModelMultipleChoiceField(
        queryset=Class.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    assigned_sections = forms.ModelMultipleChoiceField(
        queryset=Section.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    assigned_subjects = forms.ModelMultipleChoiceField(
        queryset=Subject.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )


class StudentForm(forms.ModelForm):
    """Form for creating/editing students"""
    class Meta:
        model = Student
        fields = ['roll_number', 'name', 'section', 'email', 'phone']
        widgets = {
            'roll_number': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Roll Number'
            }),
            'name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Student Name'
            }),
            'section': forms.Select(attrs={
                'class': 'w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-blue-500'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Email (optional)'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Phone (optional)'
            })
        }


class AttendanceFilterForm(forms.Form):
    """Form for filtering attendance by class, section, subject, and date"""
    class_ref = forms.ModelChoiceField(
        queryset=Class.objects.all(),
        required=True,
        label="Class",
        widget=forms.Select(attrs={
            'class': 'w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-blue-500',
            'id': 'id_class'
        })
    )
    section = forms.ModelChoiceField(
        queryset=Section.objects.none(),
        required=True,
        label="Section",
        widget=forms.Select(attrs={
            'class': 'w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-blue-500',
            'id': 'id_section'
        })
    )
    subject = forms.ModelChoiceField(
        queryset=Subject.objects.none(),
        required=True,
        label="Subject",
        widget=forms.Select(attrs={
            'class': 'w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-blue-500',
            'id': 'id_subject'
        })
    )
    date = forms.DateField(
        required=True,
        label="Date",
        widget=forms.DateInput(attrs={
            'class': 'w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-blue-500',
            'type': 'date',
            'id': 'id_date'
        }),
        initial=None  # Will be set in view
    )

    def __init__(self, *args, teacher=None, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Set max date to today
        self.fields['date'].widget.attrs['max'] = date.today().strftime('%Y-%m-%d')
        
        # If teacher is provided, filter classes and subjects by teacher's assignments
        if teacher:
            self.fields['class_ref'].queryset = teacher.assigned_classes.all()
            self.fields['subject'].queryset = teacher.assigned_subjects.all()
        
        # If class is selected, filter sections and subjects
        if 'class_ref' in self.data:
            try:
                class_id = int(self.data.get('class_ref'))
                self.fields['section'].queryset = Section.objects.filter(class_ref_id=class_id)
                if teacher:
                    self.fields['subject'].queryset = teacher.assigned_subjects.filter(class_ref_id=class_id)
                else:
                    self.fields['subject'].queryset = Subject.objects.filter(class_ref_id=class_id)
            except (ValueError, TypeError):
                pass


class AttendanceExportForm(forms.Form):
    """Form for exporting attendance data"""
    class_ref = forms.ModelChoiceField(
        queryset=Class.objects.all(),
        required=True,
        label="Class",
        widget=forms.Select(attrs={
            'class': 'w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-blue-500',
            'id': 'id_class'
        })
    )
    section = forms.ModelChoiceField(
        queryset=Section.objects.none(),
        required=True,
        label="Section",
        widget=forms.Select(attrs={
            'class': 'w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-blue-500',
            'id': 'id_section'
        })
    )
    subject = forms.ModelChoiceField(
        queryset=Subject.objects.none(),
        required=True,
        label="Subject",
        widget=forms.Select(attrs={
            'class': 'w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-blue-500',
            'id': 'id_subject'
        })
    )
    start_date = forms.DateField(
        required=True,
        label="Start Date",
        widget=forms.DateInput(attrs={
            'class': 'w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-blue-500',
            'type': 'date',
            'id': 'id_start_date'
        })
    )
    end_date = forms.DateField(
        required=True,
        label="End Date",
        widget=forms.DateInput(attrs={
            'class': 'w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-blue-500',
            'type': 'date',
            'id': 'id_end_date'
        }),
        initial=date.today
    )

    def __init__(self, *args, teacher=None, **kwargs):
        super().__init__(*args, **kwargs)
        
        # If teacher is provided, filter classes and subjects by teacher's assignments
        if teacher:
            self.fields['class_ref'].queryset = teacher.assigned_classes.all()
            self.fields['subject'].queryset = teacher.assigned_subjects.all()
        
        # If class is selected, filter sections and subjects
        if 'class_ref' in self.data:
            try:
                class_id = int(self.data.get('class_ref'))
                self.fields['section'].queryset = Section.objects.filter(class_ref_id=class_id)
                if teacher:
                    self.fields['subject'].queryset = teacher.assigned_subjects.filter(class_ref_id=class_id)
                else:
                    self.fields['subject'].queryset = Subject.objects.filter(class_ref_id=class_id)
            except (ValueError, TypeError):
                pass
