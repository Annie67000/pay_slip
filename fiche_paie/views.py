from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import Employe
from .serializers import EmployeSerializer



# Création d'un API avec méthode GET et 'AllowAny' pour la permission (Permettre tout)
@api_view(['GET'])
@permission_classes([AllowAny])
def test_fiche_paie(request):
    return Response(
        {'message': 'test fiche de paie'}
    ) 
    
    
# Récupérer la liste des employés
@api_view(['GET'])
@permission_classes([AllowAny])
def list_employees(request):
    if request.method == 'GET':
        # Récupérer tous les employés (all)
        employees = Employe.objects.all()
        
        # Sérialiser les données des employés
        serializer = EmployeSerializer(employees, many=True)
        
        # Retourner la réponse avec les données sérialisées
        return Response(serializer.data)
        
        