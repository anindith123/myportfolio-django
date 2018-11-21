from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url('', views.contact, name="contact_home"),
]