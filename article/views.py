from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404

from article.models import Produit
from rest_framework import viewsets
from .serializers import ProduitSerializer

utilisateur  = get_user_model()

class ProduitViewSet(viewsets.ModelViewSet):
    queryset = Produit.objects.all()
    serializer_class = ProduitSerializer

# Create your views here.
def accueil(request):
    paginator = Paginator(Produit.objects.all(), 5)
    page = request.GET.get('page')
    produits = paginator.get_page(page)
    return render(request,'article/produit/index.html',{'produits':produits})

def addProduct(request):
    if request.method == 'POST':
        libelle = request.POST['libelle']
        prix = request.POST['prix']
        quantite = request.POST['quantite']
        Produit.objects.create(libelle=libelle, prix=prix, quantite=quantite)
    return redirect('accueil')

def deleteProduct(request, id):
    produit = get_object_or_404(Produit, pk=id)
    produit.delete()
    return redirect('accueil')
def getProduit(request,id):
    produit = get_object_or_404(Produit, pk=id)
    return render(request,'article/produit/update.html',{'produit':produit})

def updateProduct(request):
    if request.method == 'POST':
        produit = get_object_or_404(Produit, pk=request.POST['id'])
        produit.libelle = request.POST['libelle']
        produit.prix = request.POST['prix']
        produit.quantite = request.POST['quantite']
        produit.save()
    return redirect('accueil')

def utilisateurVue(request):
    return render(request,'article/utilisateur/index.html')
def addUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        adresse = request.POST['adresse']
        prenom = request.POST['prenom']
        photo = request.FILES.get('photo')
        utilisateur.objects.create_user(
            username=username, email=email,password=password,
            adresse=adresse,
            last_name=prenom,
            photo=photo
        )
    return redirect('accueil')