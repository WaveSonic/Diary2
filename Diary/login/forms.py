from .models import User, Student, Teacher
from django import forms
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['lastname', 'password']
        widgets = {
            'lastname': TextInput(attrs={
                'class': "form-control",
                'id': "username",
                'name': "username",
                'autocomplete': 'off'

            }),
            'password': TextInput(attrs={
                'class': "form-control",
                'type': 'password',
                'id': 'password',
                'name': 'password',
                'autocomplete': 'new-password'
            }),
        }

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['lastname', 'name', 'parent_name', 'password', 'gradebook_number']
        widgets = {
            'lastname': forms.TextInput(attrs={
                'class': "form-control",
                'autocomplete': 'off',
            }),
            'name': forms.TextInput(attrs={
                'class': "form-control",
                'autocomplete': 'off',
            }),
            'parent_name': forms.TextInput(attrs={
                'class': "form-control",
                'autocomplete': 'off'
            }),
            'password': forms.PasswordInput(attrs={
                'class': "form-control",
                'autocomplete': 'new-password'
            }),
            'gradebook_number': forms.TextInput(attrs={
                'class': "form-control",
                'autocomplete': 'off'
            }),
        }


class TeacherRegistrationForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['lastname', 'name', 'parent_name', 'password', 'subject']
        widgets = {
            'lastname': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': "Прізвище"
            }),
            'name': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': "Ім'я"
            }),
            'parent_name': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': "По-батькові"
            }),
            'password': forms.PasswordInput(attrs={
                'class': "form-control",
                'placeholder': "Пароль"
            }),
            'subject': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': "Предмет викладання"
            }),
        }