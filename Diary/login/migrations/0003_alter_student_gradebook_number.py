# Generated by Django 5.1.1 on 2024-09-13 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_student_teacher_remove_user_return_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='gradebook_number',
            field=models.CharField(max_length=20, unique=True, verbose_name='Номер залікової книги'),
        ),
    ]
