import datetime
import email
from turtle import title
from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse, HttpResponse as HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, CreateView, UpdateView
from app.forms import BordereauLivraisonForm, ClientForm, FactureForm, RapportForm
from django.contrib.auth.models import User

from app.models import BordereauLivraison, Client, Facture, Rapport

# Create your views here.


def index(request):
    if request.user.is_authenticated:
        return redirect("dash-view")
    
    users = User.objects.all()
    if users.count() == 0:
        return redirect("signup")
    
    # return redirect("admin:login")
    return redirect(reverse('admin:login') + '?next=/')


def signup(request):
    users = User.objects.all()

    if users.count() > 0:
        # return redirect("admin:login")
        return redirect(reverse('admin:login') + '?next=/')
    
    if request.method == "POST":

        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:
            return render(request, "accounts/signup.html", {"error": "Les mots de passe doivent êtres identiques"}) 

        user = User.objects.create_superuser(username, email, password1)

        if user:
            # return redirect("admin:login")
            return redirect(reverse('admin:login') + '?next=/')
        
        return render(request, "accounts/signup.html", {"error": "Impossible de créer l'utilisateur"})         

    return render(request, "accounts/signup.html") 


# Début DashBoard
class DashView(TemplateView):
    template_name = "pages/index.html"
    # template_name = "pages/form.html"


# Début BL
class BordereauLivraisonView(ListView):
    model = BordereauLivraison
    paginate_by = 10
    # context_object_name = ""
    template_name = "pages/bl.html"

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        
        if kwargs.get('pk', False):
            self.model = None
            self.queryset = BordereauLivraison.objects.filter(pk = kwargs["pk"])
        
        return super().dispatch(request, *args, **kwargs)

class BordereauLivraisonCreateView(CreateView):
    model = BordereauLivraison
    form_class = BordereauLivraisonForm
    template_name = "pages/form.html"
    success_url = reverse_lazy("bl-list")
    initial = { 
        "date_livraison": datetime.date.today(),
        "facture": None
    }

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        
        if kwargs.get('pk', False):
            facture = Facture.objects.get(pk = kwargs["pk"])
            self.initial['facture'] = facture
        
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form: BaseModelForm) -> HttpResponse:

        if self.request.user.is_authenticated:
            form.instance.creator = self.request.user

        return super().form_valid(form)
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        context['title'] = "Création d'un bordereau de livraison"

        return context

# Fin BL

# Début Client
class ClientView(ListView):
    model = Client
    paginate_by = 10
    # context_object_name = ""
    template_name = "pages/client.html"

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        
        if kwargs.get('pk', False):
            self.model = None
            self.queryset = Client.objects.filter(pk = kwargs["pk"])
        
        return super().dispatch(request, *args, **kwargs)

class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm 
    template_name = "pages/form.html"
    success_url = reverse_lazy("client-list")

    def form_valid(self, form: BaseModelForm) -> HttpResponse:

        if self.request.user.is_authenticated:
            form.instance.creator = self.request.user

        return super().form_valid(form)
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        context['title'] = "Création d'un nouveau client"

        return context
    
class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    template_name = "pages/form.html"
    success_url = reverse_lazy("client-list")
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        context['title'] = "Modification d'un client"

        return context
    
# Fin Client


# Début Facture
class FactureView(ListView):
    model = Facture
    paginate_by = 10
    # context_object_name = ""
    template_name = "pages/facture.html"

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        
        if kwargs.get('pk', False):
            self.model = None
            self.queryset = Facture.objects.filter(pk = kwargs["pk"])
        
        return super().dispatch(request, *args, **kwargs)

class FactureCreateView(CreateView):
    model = Facture
    form_class = FactureForm
    template_name = "pages/form.html"
    # success_url = reverse_lazy("report-facture-create", kwargs={"pk": "auth"})
    initial = { 
        "date_facture": datetime.date.today(),
    }

    def get_success_url(self):
        return reverse('report-facture-create', kwargs={"pk": self.object.pk})

    def form_valid(self, form: BaseModelForm) -> HttpResponse:

        if self.request.user.is_authenticated:
            form.instance.creator = self.request.user

        return super().form_valid(form)
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        context['title'] = "Création d'une facture 1/2"

        return context
    
class FactureUpdateView(UpdateView):
    model = Facture
    form_class = FactureForm
    template_name = "pages/form.html"
    # success_url = reverse_lazy("facture-list")

    def get_success_url(self):
        return reverse('report-update', kwargs={"pk": self.object.pk})
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        context['title'] = "Modification d'une facture 1/2"

        return context

# Fin Facture

# Début Rapport 
    
class ReportView(ListView):
    model = Rapport
    paginate_by = 10
    # context_object_name = ""
    template_name = "pages/report.html"


class ReportCreateView(CreateView):
    model = Rapport
    form_class = RapportForm
    template_name = "pages/form.html"
    success_url = reverse_lazy("facture-list")

    def form_valid(self, form: BaseModelForm) -> HttpResponse:

        if self.kwargs.get('pk', False):
            form.instance.facture = Facture.objects.get(pk = self.kwargs["pk"])

        if self.request.user.is_authenticated:
            form.instance.creator = self.request.user

        return super().form_valid(form)
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        context['title'] = "Création d'une facture  2/2"

        return context
    
class ReportUpdateView(UpdateView):
    model = Rapport
    form_class = RapportForm
    template_name = "pages/form.html"
    success_url = reverse_lazy("facture-list")
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        context['title'] = "Modification d'une facture 2/2"

        return context

# Fin Rapport