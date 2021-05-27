"""MiraWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from blog import views
from blog.views import auth, Post, Account, Search

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', views.home, name='home'),
    path('sign_in/', auth.Sign_in, name='login'),
    path('login/', auth.login, name='login_confirm'),
    path('logout/', auth.logout, name='logout'),
    path('register_form/', auth.register_form),
    path('register/', auth.register, name='register'),
    path('feed/', Post.feed_show, name='feed'),
    path('feed_confirm', Post.add, name='add_feed'),
    path('delete_post/<int:id>', Post.delete, name='post_delete'),
    path('edit_title/<int:id>', Post.edit_name, name='edit_title'),
    path('edit_info/<int:id>', Post.edit_info, name='edit_info'),
    path('edit_link/<int:id>', Post.edit_link, name='edit_link'),
    path('account/<int:id>', Account.Profile, name='account'),
    path('edit_firstname/<int:id>', Account.edit_firstname, name='edit_firstname'),
    path('edit_lastname/<int:id>', Account.edit_lastname, name='edit_lastname'),
    path('edit_email/<int:id>', Account.edit_email, name='edit_email'),
    path('search_result', Search.show, name="search_result")
]
