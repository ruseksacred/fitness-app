from django.urls import path
from . import views

urlpatterns = [
    path('dodaj/', views.add_training, name='add_training'),
    path('historia/', views.training_history, name='training_history'),
    path('run-migrate/', views.run_migrate),
    path('show-tables/', views.show_tables),
    path('drop-old-training-table/', views.drop_old_training_table),
    path('reset-training-migrations/', views.reset_training_migrations),
]
