from django.shortcuts import render, redirect
from .forms import TrainingSessionForm

def home(request):
    return render(request, 'training/home.html')

def add_training(request):
    if request.method == "POST":
        form = TrainingSessionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_training')
    else:
        form = TrainingSessionForm()

    return render(request, 'training/add_training.html', {'form': form})

# Create your views here.
