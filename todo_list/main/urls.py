"""todo_list URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from webapp.views import index_view, create_task_view, delete_task_view, done_task_view, edit_task_view, in_progress_task_view, delete_done_tasks


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='task_index'),
    path('task/create', create_task_view, name='task_create'),
    path('task/<int:task_pk>/delete', delete_task_view, name='task_delete'),
    path('task/<int:task_pk>/done', done_task_view, name='task_done'),
    path('task/<int:task_pk>/edit', edit_task_view, name='task_edit'),
    path('task/<int:task_pk>/in_progress', in_progress_task_view, name='task_in_progress'),
    path('task/delete_all', delete_done_tasks, name='done_task_delete'),
]
