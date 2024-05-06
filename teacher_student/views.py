from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistrationUserForm, LoginUserForm, UserAccountChangeForm, TaskForm, FileForm, BoardForm
from .models import CustomUser, Board, Task, BoardComment
from django.http import HttpResponseBadRequest


def home(request):
    """Главная страница"""
    unread_count = 0
    if request.user.is_authenticated:
        unread_count = Task.objects.filter(read=False, assigned_to=request.user).count()
    return render(request, 'home.html', {'unread_count': unread_count})


@login_required
def board(request):
    """Доска"""
    boards = Board.objects.all()
    unread_count = Task.objects.filter(read=False, assigned_to=request.user).count()
    return render(request, 'board.html', {'boards': boards, 'unread_count': unread_count})


@login_required
def add_board(request):
    """Доска добавить"""
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False)
            board.created_by = request.user
            board.save()
            return redirect('board')
    else:
        form = BoardForm()
    return render(request, 'add_board.html', {'form': form})


@login_required
def board_detail(request, board_id):
    """Доска информация"""
    board = get_object_or_404(Board, id=board_id)
    unread_count = Task.objects.filter(read=False, assigned_to=request.user).count()
    return render(request, 'board_detail.html', {'board': board, 'unread_count': unread_count})


@login_required
def add_comment(request, board_id):
    """Доска комментарии"""
    board = get_object_or_404(Board, id=board_id)
    if request.method == 'POST':
        text = request.POST.get('text')
        if not text.strip():
            return HttpResponseBadRequest("Текст комментария не может быть пустым")
        author = request.user
        BoardComment.objects.create(board=board, author=author, text=text)
    return redirect('board_detail', board_id=board_id)


@login_required
def task(request):
    """Задание"""
    if request.user.is_teacher():
        tasks = Task.objects.filter(created_by=request.user)
    elif request.user.is_student():
        tasks = Task.objects.filter(assigned_to=request.user)
    else:
        tasks = Task.objects.none()
    unread_count = Task.objects.filter(read=False, assigned_to=request.user).count()
    tasks_to_update = Task.objects.filter(read=False, assigned_to=request.user)
    tasks_to_update.update(read=True)
    task_form = TaskForm(request.POST or None)
    file_form = FileForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if task_form.is_valid() and file_form.is_valid():
            task = task_form.save(commit=False)
            task.created_by = request.user
            task.save()
            file_instance = file_form.save(commit=False)
            file_instance.task = task
            file_instance.save()
            return redirect('task')
    show_form = request.user.is_authenticated and request.user.role == CustomUser.TEACHER
    return render(request, 'tasks.html', {'tasks': tasks, 'task_form': task_form, 'file_form': file_form, 'show_form': show_form, 'unread_count': unread_count, 'tasks_to_update': tasks_to_update})


def user_registration(request):
    """Регистрация"""
    if request.method == 'POST':
        form = RegistrationUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RegistrationUserForm()
    return render(request, 'registration.html', {'form': form})


def user_login(request):
    """Вход на портал"""
    if request.method == 'POST':
        form = LoginUserForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            error = "Заполните все поля"
            return render(request, 'login.html', {
                'form': form,
                'error': error
            })
    else:
        form = LoginUserForm()
    return render(request, 'login.html', {
        'form': form,
    })


def user_logout(request):
    """Выход из портала"""
    logout(request)
    return redirect('/')


@login_required
def user_account(request, user_id):
    """Аккаунт"""
    user = get_object_or_404(CustomUser, id=user_id)
    if request.method == 'POST':
        form = UserAccountChangeForm(request.POST, request.FILES, instance=user)
        if form.is_valid():  # Добавляем проверку на уникальность email
            form.save()
            return redirect('user_account', user_id=user_id)
    else:
        form = UserAccountChangeForm(instance=user)
    unread_count = Task.objects.filter(read=False, assigned_to=request.user).count()
    return render(request, 'account.html', {
        'form': form,
        'user': user,
        'unread_count': unread_count
    })
