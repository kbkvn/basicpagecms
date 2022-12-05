"""basicpagecms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from cmsapp.views import index, login, logout_view, home, createinfo, editinfo, analytics, login_auth, manage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('login', login),
    path('auth/', login_auth),
    path('logout', logout_view),
    path('home', home),
    path('manage', manage),
    path('manage/create', createinfo.as_view()),
    path('manage/edit/<int:pk>', editinfo.as_view()),
    path('data', analytics),
]
