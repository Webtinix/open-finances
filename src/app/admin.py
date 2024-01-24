from django.contrib import admin
from app.forms import BordereauLivraisonForm, ClientForm, FactureForm

# Register your models here.
from app.models import Client, BordereauLivraison, Facture, Rapport

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    
    form = ClientForm

    list_display = (
        "denomination",
        "signe",
        "numero_enreg",
    )

    search_fields = (
        "denomination",
        "signe",
        "numero_enreg",
    )

    # list_filter = ("",)

    list_per_page = 10

@admin.register(BordereauLivraison)
class BLAdmin(admin.ModelAdmin):
    
    form = BordereauLivraisonForm

    list_display = (
        "date_livraison",
        "numero_bl",
        "facture",
    )

    search_fields = (
        "date_livraison",
        "numero_bl",
        "facture",
    )

    # autocomplete_fields = (
    #     "facture",
    # )

    # list_filter = ("",)

    list_per_page = 10

class RapportInline(admin.TabularInline):
    model = Rapport
    extra = 1
    max_num = 1
    min_num = 1

@admin.register(Facture)
class FactureAdmin(admin.ModelAdmin):
    inlines = [
        RapportInline,
    ]

    form = FactureForm

    list_display = (
        "numero_ordre",
        "date_facture",
        "montant_total",
        "nombre_bouteilles",
        "poids_bouteilles",
        "total_par_categories",
        "client",
    )

    search_fields = (
        "numero_ordre",
        "date_facture",
        "montant_total",
        "nombre_bouteilles",
        "poids_bouteilles",
        "total_par_categories",
        "client",
    )

    list_per_page = 10

