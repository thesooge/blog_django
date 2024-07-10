from django.shortcuts import render
from django.views import generic
# Create your views here.
from .forms import UserCreationForm
from .models import CustomUser


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    model = CustomUser

