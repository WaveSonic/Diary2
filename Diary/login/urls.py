from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register-student', views.register_student, name='register-student'),
    path('register-teacher', views.register_teacher, name='register-teacher')
]
