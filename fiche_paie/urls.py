from .views import test_fiche_paie, list_employees
from django.urls import path


urlpatterns = [
    path('test', test_fiche_paie, name='test_fiche_paie'),
    path('employees', list_employees, name='Liste des employés'),
]