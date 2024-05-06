from django.contrib import admin

from teacher_student.models import CustomUser, Board, BoardComment, Task, File


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    """Пользователь"""
    fieldsets = (
        ('ЛИЧНЫЕ ДАННЫЕ', {
            'fields': ('username', 'fio', 'role', 'last_login', 'date_joined',)},),
        ('РАЗРЕШЕНИЯ', {
            'classes': ('collapse',),
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    list_display = 'username', 'fio', 'is_active', 'role',
    list_editable = 'is_active',
    list_filter = 'is_active', 'role',
    readonly_fields = 'last_login', 'date_joined',
    search_fields = 'username', 'fio',
    search_help_text = 'Поиск по логину, имени ФИО и номеру телефона'
    list_per_page = 20


class BoardCommentline(admin.TabularInline):
    """Коментарий"""
    model = BoardComment
    extra = 0


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    """Доска"""
    list_display = 'title', 'created_at', 'created_by',
    list_filter = 'created_at', 'created_by',
    inlines = BoardCommentline,
    list_per_page = 20


class FileInline(admin.TabularInline):
    """Файл"""
    model = File
    extra = 0


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    """Задание"""
    list_display = 'title', 'created_at', 'created_by', 'assigned_to', 'read',
    list_filter = 'created_at', 'created_by', 'assigned_to', 'read',
    list_editable = 'read',
    inlines = FileInline,
    list_per_page = 20
