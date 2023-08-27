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
from django.core.mail import send_mail
from django.conf import settings
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.text import MIMEText
import smtplib
from django.conf import settings
from django.shortcuts import render
from .models import Video




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
    photos = Image.objects.all()  # Récupère toutes les photos de la base de données
    videos = Video.objects.all()
    return render(request, 'pages/admi.html', {'photos': photos, 'videos': videos})
     

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
    return render(request, 'pages/admi.html')


#def photo(request):
    photos = Image.objects.all()  # Récupère toutes les photos de la base de données
    return render(request, 'pages/admi.html', {'photos': photos})

def photo_list(request):
    photos = Image.objects.all()  # Récupère toutes les photos de la base de données
    videos = Video.objects.all() # Récupère toutes les photos de la base de données
    return render(request, 'pages/photo.html', {'photos': photos, 'videos': videos})



    


#def delete_image(request, image_id):
    image = get_object_or_404(Image, id=image_id)
    if request.method == 'POST':
        image.image.delete()  # Supprime le fichier image du système de fichiers
        image.delete()  # Supprime l'objet Image de la base de données
        return redirect('admi')  # Redirigez vers la page utilisateur ou toute autre page souhaitée
    return render(request, 'pages/admi.html', {'image': image})
def delete_image(request, image_id):
    if request.method == 'POST':
        try:
            image = Image.objects.get(pk=image_id)
            image.delete()
            print("Image deleted successfully")
        except Image.DoesNotExist:
            print("Image not found")
    
    return redirect('admi')

def supprimer_video(request, video_id):
    if request.method == 'POST':
        try:
            video = Video.objects.get(pk=video_id)
            video.delete()
            print("Vidéo supprimée avec succès")
        except Video.DoesNotExist:
            print("Vidéo non trouvée")
    
    return redirect('admi')




def contact(request):
    message_sent = False
    
    if request.method == 'POST':
        
        subject = request.POST['subject']
        email = request.POST['email']
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        message = request.POST['message']
        
        try:
            msg = MIMEText(message)
            msg['Subject'] = subject
            msg['From'] = f'{first_name} {last_name} <{email}>'  # Utilisation du nom et de l'adresse e-mail comme expéditeur
            msg['To'] = settings.EMAIL_HOST_USER
            msg.add_header('Reply-To', email)  # Adresse e-mail pour répondre à l'utilisateur
            
            server = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
            server.starttls()
            server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
            server.sendmail(email, [settings.EMAIL_HOST_USER], msg.as_string())
            server.quit()
            
            message_sent = True
        except Exception as e:
            print("Erreur lors de l'envoi d'e-mail:", str(e))
    
    return render(request, 'pages/index.html', {'message_sent': message_sent})

def ajouter_video(request):
    if request.method == 'POST':
        titre = request.POST['titre']
        lien = request.POST['lien']
        
        
        
        nouvelle = Video.objects.create(
            titre=titre,
            lien=lien,
        )
        nouvelle.save()
        print('titre')
        return redirect('admi')
    
    return render(request, 'pages/admi.html')

#def afficher_videos(request):
    videos = Video.objects.all()
    for video in videos:
       print(video.titre)
    return render(request,'pages/photo.html', {'videos': videos})



        

        




   

    




    
