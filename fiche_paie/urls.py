from .views import test_fiche_paie
from django.urls import path


urlpatterns = [
    path('test', test_fiche_paie, name='test_fiche_paie')
]