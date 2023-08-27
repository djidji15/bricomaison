from django.urls import path 
from . import views 


urlpatterns = [

    path('cnx/', views.cnx, name='cnx'),
    path('admi/', views.admi, name='admi'),
    path('logout/', views.logout_view, name='logout'),
    path('change_password/', views.change_password, name='change_password'),
    path('ajou/', views.add_image, name='add_image'),
    path('delete_image/<int:image_id>/', views.delete_image, name='delete_image'),
    path('con/', views.contact, name='contact'),
    path('ph/', views.photo_list, name='photo_list'),
    path('ajt/', views.ajouter_video, name='ajouter_video'),
    #path('ajt/', views.afficher_videos, name='afficher_videos'),
    #path('photo/', views.photo, name='photo'),
    path('supprimer_video/<int:video_id>/', views.supprimer_video, name='supprimer_video'),

    
   
    
    
 
    
    
    
 ]