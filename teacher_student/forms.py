from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from teacher_student.models import CustomUser, Task, File, Board


class RegistrationUserForm(UserCreationForm):
    """Регистрация"""

    class Meta:
        model = CustomUser
        fields = 'username', 'password1', 'password2', 'fio', 'role',

    def __init__(self, *args, **kwargs):
        super(RegistrationUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Обязательное для заполнения'
        self.fields['password1'].widget.attrs['placeholder'] = 'Обязательное для заполнения'
        self.fields['password2'].widget.attrs['placeholder'] = 'Обязательное для заполнения'
        self.fields['fio'].widget.attrs['placeholder'] = 'Обязательное для заполнения'
        self.fields['role'].widget.attrs['placeholder'] = 'Обязательное для заполнения'


class LoginUserForm(AuthenticationForm):
    """Вход"""
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserAccountChangeForm(forms.ModelForm):
    """Аккаунт"""

    class Meta:
        model = CustomUser
        fields = 'fio',
        help_texts = {'fio': 'Укажите полностью Фамилию Имя Отчество', }


class TaskForm(forms.ModelForm):
    """Задание"""

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['assigned_to'].queryset = CustomUser.objects.filter(role=CustomUser.STUDENT)

    class Meta:
        model = Task
        fields = 'title', 'description', 'assigned_to'


class FileForm(forms.ModelForm):
    """Файл"""

    class Meta:
        model = File
        fields = 'files',


class BoardForm(forms.ModelForm):
    """Доска"""

    class Meta:
        model = Board
        fields = 'title', 'description',
