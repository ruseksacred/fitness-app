from django.urls import path
from . import views

urlpatterns = [
    path('dodaj/', views.add_training, name='add_training')
]
