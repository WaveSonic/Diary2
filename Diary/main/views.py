from django.shortcuts import render

def home_student(request):
    data = {
        'title': "Домашня сторінка"
    }
    return render(request, 'login/home.html', data)
