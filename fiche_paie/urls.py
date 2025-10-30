from .views import test_fiche_paie, employe_list_create
from django.urls import path


urlpatterns = [
    path('test', test_fiche_paie, name='test_fiche_paie'),
    path('employees', employe_list_create , name='Employés'),
]