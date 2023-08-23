from django.urls import path 
from . import views 

urlpatterns = [

    path('cnx/', views.cnx, name='cnx'),
    path('admi/', views.admi, name='admi'),
    path('logout/', views.logout_view, name='logout'),
    path('change_password/', views.change_password, name='change_password'),
    path('ajou/', views.add_image, name='add_image'),
    path('del/', views.delete_image, name='delete_image'),
    
    path('ph/', views.photo, name='photo'),
 
    
    
    
 ]