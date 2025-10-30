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

@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def employe_list_create(request):
    # --------------------------------------------------------------------
    # GET | Récupérer la liste des employés
    # --------------------------------------------------------------------
    if request.method == 'GET':
        employees = Employe.objects.all()
        serializer = EmployeSerializer(employees, many=True)
        return Response(serializer.data)
    
    # --------------------------------------------------------------------
    # POST | Ajouter un nouvel employé
    # --------------------------------------------------------------------
    elif request.method == 'POST':
        # Pas besoin de vérifier 'if request.method == 'POST':' car on utilise 'elif'
        serializer = EmployeSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)  # 201 Created
        return Response(serializer.errors, status=400)    # 400 Bad Request
        