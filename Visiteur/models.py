from django.db import models
from auditlog.models import AuditlogHistoryField


class Visiteur(models.Model):

    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )

    CIN = models.CharField(max_length=200, unique=True)
    Genre = models.CharField(max_length=200, null=True, choices=GENDER_CHOICES)
    Prenom_v = models.CharField(max_length=200, null=True)
    Nom_V = models.CharField(max_length=200, null=True)
    history = AuditlogHistoryField()  # Champ pour stocker l'historique des modifications
    def __str__(self):
        return self.Nom_V

class MessageReservation(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField()
    date_reservation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message de réservation par {self.nom}"