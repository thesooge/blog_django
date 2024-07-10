from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    # path('', views.HomePage.as_view(), name = 'home'),
    path('about', views.AboutPage.as_view(), name='about'),
    path('contact', views.Contact.as_view(), name='contact'),
    path('profile', views.Profile.as_view(), name='profile'),

]