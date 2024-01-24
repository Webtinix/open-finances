from collections.abc import Mapping
from dataclasses import field, fields
from typing import Any
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from django.db.models import Exists, OuterRef

from app.models import BordereauLivraison, Client, Facture, Rapport
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User


""" class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields """


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = [
            "denomination",
            "signe",
            "numero_enreg",
        ]
        labels = {
            "denomination": "Dénomination",
            "signe": "Signe",
            "numero_enreg": "Numéro d'enregistrement",
        }

class FactureForm(forms.ModelForm):
    class Meta:
        model = Facture
        fields = [
            "numero_ordre",
            "date_facture",
            "montant_total",
            "client",
        ]
        labels = {
            "numero_ordre": "Numéro d'ordre",
            "date_facture": "Date",
            "montant_total": "Montant total",
            "client": "Client",
        }
        widgets = {
            "date_facture": forms.SelectDateWidget(
                
            )
        }

class BordereauLivraisonForm(forms.ModelForm):
    class Meta:
        model = BordereauLivraison
        fields = [
            "date_livraison",
            "numero_bl",
            "facture",
        ]
        labels = {
            "date_livraison": "Date de livraison",
            "numero_bl": "Numéro du BL",
            "facture": "Facture",
        }
        widgets = {
            "date_livraison": forms.SelectDateWidget(
                
            )
        }

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        
        self.fields['facture'].queryset = Facture.objects.filter(~Exists(
            BordereauLivraison.objects.filter(facture = OuterRef("pk"))
        ))

class RapportForm(forms.ModelForm):
    class Meta:
        model = Rapport
        fields = [
            "nombre_bouteilles",
            "poids_bouteilles",
            "total_par_categories",
        ]
        labels = {
            "nombre_bouteilles": "Nombre bouteilles",
            "poids_bouteilles": "Poids bouteille",
            "total_par_categories": "Total par catégories",
        }

""" FactureRapportFormSet = forms.inlineformset_factory(Facture, Rapport, fields=[
    "numero_ordre",
    "date_facture",
    "montant_total",
    "client",
    "nombre_bouteilles",
    "poids_bouteilles",
    "total_par_categories",
]) """