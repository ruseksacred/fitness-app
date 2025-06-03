from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TrainingSessionForm
from .models import TrainingSessionNew

def home(request):
    return render(request, 'training/home.html')

@login_required
def add_training(request):
    if request.method == "POST":
        form = TrainingSessionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_training')
    else:
        form = TrainingSessionForm()

    return render(request, 'training/add_training.html', {'form': form})

@login_required
def training_history(request):
    trainings = TrainingSessionNew.objects.filter(user=request.user).order_by('-date')
    return render(request, 'training/training_history.html', {'trainings': trainings})

# Create your views here.
