"""
URL configuration for t_config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from teacher_student.views import home, board, add_board, board_detail, add_comment, user_registration, user_login, user_logout, user_account, task

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('task/', task, name='task'),
    path('board/', board, name='board'),
    path('add_board/', add_board, name='add_board'),
    path('board/<int:board_id>/', board_detail, name='board_detail'),
    path('add_comment/<int:board_id>/', add_comment, name='add_comment'),
    path('registration/', user_registration, name='user_registration'),
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
    path('user_account/<int:user_id>/', user_account, name='user_account'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
