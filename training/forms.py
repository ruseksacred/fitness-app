from django import forms
from .models import TrainingSessionNew

class TrainingSessionForm(forms.ModelForm):
    class Meta:
        model = TrainingSessionNew
        fields = ['date', 'exercise', 'sets', 'repetitions', 'weight', 'notes']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'notes': forms.Textarea(attrs={'rows': 2}),
        }