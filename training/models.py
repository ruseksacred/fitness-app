from django.db import models
from django.contrib.auth.models import User

class TrainingSessionNew(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='training_sessions')
    EXERCISES = [
        ('pushups', 'Pompki'),
        ('situps', 'Brzuszki'),
        ('squats', 'Przysiady'),
        ('biceps', 'Biceps'),
        ('triceps', 'Triceps'),
        ('shoulders', 'Barki'),
    ]

    date = models.DateField()
    exercise = models.CharField(max_length=20, choices=EXERCISES)
    sets = models.PositiveIntegerField()
    repetitions = models.PositiveIntegerField()
    weight = models.FloatField(null=True, blank=True, help_text="Waga ciała podczas treningu (kg)")
    notes = models.TextField(blank=True)
    temp_field = models.CharField(max_length=10, default='tmp', blank=True)  # tymczasowe pole

    def __str__(self):
        return f"{self.get_exercise_display()} - {self.date}"

# Create your models here.
