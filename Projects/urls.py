from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url('', views.home, name="project_home"),
]
