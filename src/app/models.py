from django.db import models


# Create your models here.
class Client(models.Model):
    denomination = models.CharField(max_length=100)
    signe = models.CharField(max_length=100)
    numero_enreg = models.CharField(max_length=100)


class Facture(models.Model):
    numero_ordre = models.CharField(max_length=100)
    date_facture = models.DateField()
    montant_total = models.IntegerField()
    client = models.ForeignKey(Client, on_delete=models.PROTECT)

class Rapport(models.Model):
    nombre_bouteilles = models.IntegerField(default=0)
    poids_bouteilles = models.IntegerField(default=0)
    total_par_categories = models.IntegerField(default=0)
    facture = models.ForeignKey(Facture, on_delete=models.CASCADE)


class BordereauLivraison(models.Model):
    date_livraison = models.DateField()
    numero_bl = models.CharField(max_length=100)
    facture = models.ForeignKey(Facture, on_delete=models.CASCADE)