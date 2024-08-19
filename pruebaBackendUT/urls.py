"""
URL configuration for pruebaBackendUT project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from personas.views import all_users, add_user, add_movie, edit_user,delete_user, user_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', all_users, name='all_users'),
    path('add/', add_user, name='add_user'),
    path('add_movie/', add_movie, name='add_movie'),
    path('<int:user_id>/edit/', edit_user, name='edit_user'),
    path('<int:user_id>/delete/', delete_user, name='delete_user'),
    path('users/', user_list, name='user_list'),

]

