"""
my_django15_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

app_name = 'home'
urlpatterns = [
    # /home/dashboard/
    url(r'^dashboard/$', views.dashboard, name='dashboard'),

    # /home/take_attendance/
    url(r'^take_attendance/(?P<lecture>[A-Z]*[-]*)/(?P<class_name>[1-8]{0,1}[A-Z]{0,4}[1-4]{0,1}[-]*)/$', views.take_attendance, name='take_attendance'),

    # /home/modify_attendance/
    url(r'^modify_attendance/$', views.modify_attendance, name='modify_attendance'),

    # /home/view_attendance/
    url(r'^view_attendance/$', views.view_attendance, name='view_attendance'),

    # /home/view_attendance/
    url(r'^generate_report/$', views.generate_report, name='generate_report'),

    # /home/signout/
    url(r'^signout/$', views.signout, name='signout'),
]
