from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import login
import logging

def register(request):
    try:
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')  # Redirect to login page after registration
        else:
            form = CustomUserCreationForm()
        return render(request, 'users/register.html', {'form': form})
    except Exception as e:
        logging.exception("Error during user registration: %s", e)
        

# Create your views here.
