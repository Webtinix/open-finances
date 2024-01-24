from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Client(models.Model):
    denomination = models.CharField(max_length=100, verbose_name="Dénomination",)
    signe = models.CharField(max_length=100, verbose_name="Signe",)
    numero_enreg = models.CharField(max_length=100, verbose_name="Numéro d'enregistrement",)
    creator = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Créateur",)
    date_creation = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="Date de création",)
    date_update = models.DateTimeField(auto_now=True, editable=False, verbose_name="Date de modification",)

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"

    def __str__(self):
        return self.denomination


class Facture(models.Model):
    numero_ordre = models.CharField(max_length=100, verbose_name="Numéro d'ordre",)
    date_facture = models.DateField(verbose_name="Date de la facture",)
    montant_total = models.IntegerField(verbose_name="Montant total",)
    client = models.ForeignKey(Client, on_delete=models.PROTECT, verbose_name="Client",)
    creator = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Créateur",)
    date_creation = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="Date de création",)
    date_update = models.DateTimeField(auto_now=True, editable=False, verbose_name="Date de modification",)

    class Meta:
        verbose_name = "Facture"
        verbose_name_plural = "Factures"

    def __str__(self):
        return self.numero_ordre
    
    @property
    def nombre_bouteilles(self):
        return Rapport.objects.get(facture = self).nombre_bouteilles

    @property
    def poids_bouteilles(self):
        return Rapport.objects.get(facture = self).poids_bouteilles

    @property
    def total_par_categories(self):
        return Rapport.objects.get(facture = self).total_par_categories

class Rapport(models.Model):
    nombre_bouteilles = models.IntegerField(default=0, verbose_name="Nombre de bouteilles",)
    poids_bouteilles = models.IntegerField(default=0, verbose_name="Poids de bouteilles",)
    total_par_categories = models.IntegerField(default=0, verbose_name="Total par catégories",)
    facture = models.ForeignKey(Facture, on_delete=models.CASCADE, verbose_name="Facture",)
    date_creation = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="Date de création",)
    date_update = models.DateTimeField(auto_now=True, editable=False, verbose_name="Date de modification",)

    class Meta:
        verbose_name = "Rapport"
        verbose_name_plural = "Rapports"

    def __str__(self):
        return self.facture.numero_ordre


class BordereauLivraison(models.Model):
    date_livraison = models.DateField(verbose_name="Date de livraison",)
    numero_bl = models.CharField(max_length=100, verbose_name="Numéro du bordereau",)
    facture = models.ForeignKey(Facture, on_delete=models.CASCADE, verbose_name="Facture",)
    creator = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Créateur",)
    date_creation = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="Date de création",)
    date_update = models.DateTimeField(auto_now=True, editable=False, verbose_name="Date de modification",)

    class Meta:
        verbose_name = "Bordereau de livraison"
        verbose_name_plural = "Bordereaux de livraison"

    def __str__(self):
        return self.numero_bl