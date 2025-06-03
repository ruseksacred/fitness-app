from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TrainingSessionForm
from .models import TrainingSessionNew
from django.http import HttpResponse
from django.db import connection
from django.core.management import call_command

def home(request):
    return render(request, 'training/home.html')

@login_required
def add_training(request):
    if request.method == "POST":
        # Odbierz dane z customowego formularza
        exercises_json = request.POST.get('exercises')
        duration = request.POST.get('duration')
        training_start = request.POST.get('training_start')
        # Możesz tu sparsować exercises_json i zapisać do bazy (np. tylko podsumowanie)
        # Przykład: zapis pierwszego ćwiczenia jako osobny rekord
        import json
        exercises = json.loads(exercises_json) if exercises_json else []
        for ex in exercises:
            TrainingSessionNew.objects.create(
                user=request.user,
                date=training_start[:10],  # tylko data
                exercise=ex['name'],
                sets=len(ex['series']),
                repetitions=sum(int(s['reps']) for s in ex['series']),
                weight=None,
                notes=f"Serii: {len(ex['series'])}, szczegóły: {ex['series']}"
            )
        return redirect('training_history')
    return render(request, 'training/add_training.html')
def training_history(request):
    trainings = TrainingSessionNew.objects.filter(user=request.user).order_by('-date')
    return render(request, 'training/training_history.html', {'trainings': trainings})

def run_migrate(request):
    call_command('migrate')
    return HttpResponse("Migracje wykonane!")

def show_tables(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT tablename FROM pg_tables WHERE schemaname = 'public';")
        tables = cursor.fetchall()
    return HttpResponse("<br>".join([t[0] for t in tables]))

def drop_old_training_table(request):
    with connection.cursor() as cursor:
        cursor.execute("DROP TABLE IF EXISTS training_trainingsession CASCADE;")
    return HttpResponse("Stara tabela usunięta.")

def reset_training_migrations(request):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM django_migrations WHERE app='training';")
    return HttpResponse("Usunięto wpisy migracji training.")

# Create your views here.
