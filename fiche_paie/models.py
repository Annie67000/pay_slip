from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Employe(models.Model):
    # Ceci crée la relation One-to-One vers le modèle User
    # C'est ce qui relie les deux tables.
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    
    
    matricule = models.CharField(max_length=50, unique=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(max_length=150, unique=True)
    departement = models.CharField(max_length=100, blank=True, null=True)
    poste = models.CharField(max_length=100, blank=True, null=True)
    actif = models.BooleanField(default=True)

    class Meta:
        db_table = 'employe'
        verbose_name = "Employé"
        verbose_name_plural = "Employés"

    def __str__(self):
        return f"{self.prenom} {self.nom} ({self.matricule})"


class FichePaie(models.Model):
    employe = models.ForeignKey(
        Employe, on_delete=models.CASCADE, related_name='fiches_paie'
    )
    mois = models.CharField(max_length=20)
    fichier_pdf = models.CharField(max_length=255)
    date_import = models.DateTimeField(default=timezone.now)
    envoyee = models.BooleanField(default=False)

    class Meta:
        db_table = 'fiche_paie'
        verbose_name = "Fiche de paie"
        verbose_name_plural = "Fiches de paie"

    def __str__(self):
        return f"Fiche {self.mois} - {self.employe.matricule}"

class EnvoiEmail(models.Model):
    fiche = models.ForeignKey(
        FichePaie, on_delete=models.CASCADE, related_name='envois_email'
    )
    date_envoi = models.DateTimeField(default=timezone.now)
    statut = models.CharField(max_length=50, default='en attente')
    message_erreur = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'envoi_email'
        verbose_name = "Envoi d'email"
        verbose_name_plural = "Envois d'emails"

    def __str__(self):
        return f"Envoi {self.fiche.id} - {self.statut}"
