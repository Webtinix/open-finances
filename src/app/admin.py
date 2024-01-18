from django.contrib import admin
from app.forms import BordereauLivraisonForm, ClientForm

# Register your models here.
from app.models import Client, BordereauLivraison

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