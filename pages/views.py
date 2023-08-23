from django.shortcuts import render
from django.http import HttpResponse 
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Image
from django.shortcuts import render, redirect


# Create your views here.
def cnx(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('admi')  # Rediriger vers une page après la connexion réussie
        else:
            error_message = "Identifiants invalides. Veuillez réessayer."
            return render(request, 'pages/login.html', {'error_message': error_message})
    return render(request, 'pages/login.html')

@login_required  
#def admi(request):
    
    #return render(request, 'pages/admi.html')
 
def logout_view(request):
    logout(request)
    return redirect('cnx')

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Met à jour la session de l'utilisateur
            messages.success(request, 'Votre mot de passe a été mis à jour avec succès.')
            return redirect(reverse('cnx'))  # Rediriger vers la page des paramètres après la modification du mot de passe
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'pages/change_password.html', {'form': form})

@login_required
def admi(request):
     return render(request, 'pages/admi.html')

def add_image(request):
    if request.method == 'POST':
        image_file = request.FILES.get('image')

        if image_file:
            try:
                new_image = Image(image=image_file)
                new_image.save()
                print("Image saved successfully")
            except Exception as e:
                print(f"Error saving image: {e}")
        else:
            print("No image file received")

    return redirect('admi') 

def delete_image(request, image_id):
    image = get_object_or_404(Image, id=image_id)
    if request.method == 'POST':
        image.image.delete()  # Supprime le fichier image du système de fichiers
        image.delete()  # Supprime l'objet Image de la base de données
        return redirect('admi')  # Redirigez vers la page utilisateur ou toute autre page souhaitée
    return render(request, 'pages/admi.html', {'image': image})
 

def photo_list(request):
    photos = Image.objects.all()  # Récupère toutes les photos de la base de données
    return render(request, 'pages/admi.html', {'photos': photos})

def photo(request):
    photos = Image.objects.all()  # Récupère toutes les photos de la base de données
    return render(request, 'pages/photo.html', {'photos': photos})
   

    




    
