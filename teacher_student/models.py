from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """Пользователь"""
    TEACHER = 'teacher'
    STUDENT = 'student'
    ROLE_CHOICES = [
        (TEACHER, 'Учитель'),
        (STUDENT, 'Ученик'),
    ]
    username = models.CharField(verbose_name='Логин', max_length=50, unique=True)
    fio = models.CharField(verbose_name='ФИО', help_text='Полностью', max_length=200)
    role = models.CharField(verbose_name='Роль', max_length=10, choices=ROLE_CHOICES)

    def is_teacher(self):
        return self.role == self.TEACHER

    def is_student(self):
        return self.role == self.STUDENT

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователь'
        ordering = 'fio',

    def __str__(self):
        return self.fio


class Board(models.Model):
    """Доска"""
    title = models.CharField(verbose_name='Заголовок', max_length=100)
    description = models.TextField(verbose_name='Описание')
    created_at = models.DateTimeField(verbose_name='Время создания', auto_now_add=True)
    created_by = models.ForeignKey(CustomUser, verbose_name='Кто создал запись', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Доска'
        verbose_name_plural = 'Доска'
        ordering = 'title',

    def __str__(self):
        return self.title


class BoardComment(models.Model):
    """Коментарий"""
    board = models.ForeignKey(Board, verbose_name='Доска', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(CustomUser, verbose_name='Пользователь', on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Сообщение')
    created_at = models.DateTimeField(verbose_name='Время создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарий'
        ordering = '-created_at',

    def __str__(self):
        return self.text


class Task(models.Model):
    """Задание"""
    title = models.CharField(verbose_name='Заголовок', max_length=100)
    description = models.TextField(verbose_name='Описание')
    created_at = models.DateTimeField(verbose_name='Время создания', auto_now_add=True)
    created_by = models.ForeignKey(CustomUser, verbose_name='Создал задание', on_delete=models.CASCADE, related_name='created_tasks')
    assigned_to = models.ForeignKey(CustomUser, verbose_name='Кому задание', on_delete=models.CASCADE, related_name='assigned_tasks')
    read = models.BooleanField(verbose_name='Прочитано', default=False)

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задание'
        ordering = '-created_at',

    def __str__(self):
        return self.title


class File(models.Model):
    """Файл"""
    files = models.FileField(verbose_name='Файлы', upload_to='files/', blank=True, null=True)
    task = models.ForeignKey(Task, verbose_name='Задание', on_delete=models.CASCADE, null=True, blank=True, related_name='file_task')

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'

    def __str__(self):
        return str(self.id)

    @property
    def get_file_size(self):  # Размер файла
        return self.files.size if self.files else 0
