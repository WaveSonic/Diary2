from django.shortcuts import render, redirect
from .forms import LoginForm, StudentRegistrationForm, TeacherRegistrationForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login as auth_login
from .models import Student
#TEST = Test
def home(request):
    data = {
        'title': "Домашня сторінка"
    }
    return render(request, 'login/home.html', data)

def login(request):
    error = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('lastname')
            password = form.cleaned_data.get('password')
            #Шукаэмо в БД користувача із номером залікової книжки яка співпадає із username
            try:
                student = Student.objects.get(gradebook_number=username)
                print(student.gradebook_number)
                user = authenticate(request, username=student.user.username, password=password)

                if user is not None:
                    auth_login(request, user)  # Авторизуємо користувача
                    return redirect('home_student')  # Перенаправляємо на головну сторінку або інший ресурс
                else:
                    error = 'Невірний пароль або ім\'я користувача'
            except Student.DoesNotExist:
                error = 'Користувача з таким номером залікової книжки не знайдено'

            print(error)


    data = {
        'form': LoginForm
    }

    return render(request, 'login/login.html', data)

def register_student(request):
    error = ''
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.password = make_password(form.cleaned_data['password'])
            student.save()
            return redirect('login')
        else:
            error = "Форма було невірна"
    data = {
        'form': StudentRegistrationForm
    }
    return render(request, 'login/register_student.html', data)


def register_teacher(request):
    error = ''
    if request.method == 'POST':
        form = TeacherRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            error = "Форма було невірна"

    data = {
        'form': TeacherRegistrationForm
    }
    return render(request, 'login/register_teacher.html', data)