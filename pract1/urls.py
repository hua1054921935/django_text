"""django_text URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url

from pract1.views import Meyhod1,Meyhod,large
urlpatterns = [
    url(r'^method/', Meyhod.as_view(),name='method'),
    url(r'^method1/', Meyhod1.as_view(),name='method1'),
    url(r'create_topology/',large,name='create_topology')
]
