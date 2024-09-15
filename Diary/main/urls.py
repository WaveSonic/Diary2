from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_student, name='home_student'),
]
