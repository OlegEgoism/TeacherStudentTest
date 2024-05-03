# # from django import forms
# # from django.contrib.auth.forms import AuthenticationForm
# #
# #
# # class CustomUserCreationForm(AuthenticationForm):
# #     """Вход"""
# #     username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'style': 'margin:10px; width: 300px; padding:10px; height:20px', 'class': 'form-control col-sm-8', 'placeholder': 'Логин'}))
# #     password = forms.CharField(label='Логин', widget=forms.PasswordInput(attrs={'style': 'margin:10px; width: 300px; padding:10px; height:20px', 'class': 'form-control col-sm-8', 'placeholder': 'Пароль'}))
#
# from django.contrib.auth.forms import UserCreationForm
# from .models import CustomUser
#
# class CustomUserCreationForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         model = CustomUser
#         fields = 'username', 'password', 'fio',
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from teacher_student.models import CustomUser, Task, File


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
    class Meta:
        model = Task
        fields = 'title', 'description', 'assigned_to'


class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = 'files',
