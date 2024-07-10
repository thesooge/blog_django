from django.shortcuts import render
from django.views import generic
# Create your views here.

class HomePage(generic.TemplateView):
    template_name = 'pages/home.html'

class AboutPage(generic.TemplateView):
    template_name = 'pages/about.html'    


class Contact(generic.TemplateView):
    template_name = 'pages/contact.html'

class Profile(generic.TemplateView):
    template_name = 'pages/profile.html'    