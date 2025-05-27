from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # automatyczne zalogowanie po rejestracji
            return redirect('home')  # zmień na nazwę swojej strony startowej
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

# Create your views here.
