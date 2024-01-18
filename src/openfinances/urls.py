"""
URL configuration for openfinances project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app.views import BordereauLivraisonCreateView, BordereauLivraisonView, ClientCreateView, ClientUpdateView, ClientView, DashView, FactureCreateView, FactureUpdateView, FactureView, ReportCreateView, ReportUpdateView, ReportView, index, signup


urlpatterns = [
    
    path('', index, name="index"),

    path('signup', signup, name="signup"),

    path('dashbord', DashView.as_view(), name="dash-view"),
    
    path('bls/', BordereauLivraisonView.as_view(), name="bl-list"),
    path('bl/<int:pk>', BordereauLivraisonView.as_view(), name="view-list"),
    path('bl/create', BordereauLivraisonCreateView.as_view(), name="bl-create"),
    path('bl/facture/<int:pk>/create', BordereauLivraisonCreateView.as_view(), name="bl-facture-create"),
    
    path('clients/', ClientView.as_view(), name="client-list"),
    path('client/<int:pk>', ClientView.as_view(), name="view-list"),
    path('client/create', ClientCreateView.as_view(), name="client-create"),
    path('client/<int:pk>/update', ClientUpdateView.as_view(), name="client-update"),
    
    path('factures/', FactureView.as_view(), name="facture-list"),
    path('facture/<int:pk>', FactureView.as_view(), name="view-list"),
    path('facture/create', FactureCreateView.as_view(), name="facture-create"),
    path('facture/<int:pk>/update', FactureUpdateView.as_view(), name="facture-update"),
    
    path('reports/', ReportView.as_view(), name="report-list"),
    path('report/facture/<int:pk>/create', ReportCreateView.as_view(), name="report-facture-create"),
    path('report/<int:pk>/update', ReportUpdateView.as_view(), name="report-update"),


    path('admin/', admin.site.urls),
]
