from rest_framework import serializers
from .models import Employe


# Serializer pour le modèle Employe
class EmployeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employe
        # Champs à inclure dans la sérialisation, ici on convertit toutes les champs
        fields = ['id', 'matricule', 'nom', 'prenom', 'email', 'departement', 'poste', 'actif']