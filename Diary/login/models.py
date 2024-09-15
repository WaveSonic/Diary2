from django.db import models

class User(models.Model):
    lastname = models.CharField('Прізвище', max_length=50)
    name = models.CharField('Ім\'я', max_length=50)
    parent_name = models.CharField('По-батькові', max_length=50)
    password = models.CharField('Пароль', max_length=50)

    def __str__(self):
        return f"{self.lastname} {self.name}"

    class Meta:
        verbose_name = "Користувач"
        verbose_name_plural = "Користувачі"


# Створюємо модель, що наслідує User
class Student(User):
    gradebook_number = models.CharField('Номер залікової книги', max_length=20, unique=True)

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенти"


class Teacher(User):
    subject = models.CharField('Предмет викладання', max_length=100)

    class Meta:
        verbose_name = "Викладач"
        verbose_name_plural = "Викладачі"


