"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name="home"),
    path('home/', views.index,name="home"),
    path('register/', views.register,name="register"),
    path('hots/', views.hots,name="hots"),
    path('tours/', views.tours,name="tours"),
    path('blogs/', views.blogs,name="blogs"),
    path('contacts/', views.contacts,name="contacts"),
    path('login/', views.login_user,name="login_user"),
    path('logout/', views.logout_user,name="logout_user"),
]
