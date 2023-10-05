"""
The `urlpatterns` list routes URLs to views. For more information please see:
https://docs.djangoproject.com/en/4.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('oauth2/', include(arg='oauth2_provider.urls', namespace='oauth2_provider')),
    path('accounts/', include('accounts.urls')),
]
