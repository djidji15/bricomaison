from django.urls import path 
from . import views 
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [

    path('cnx/', views.login, name='login'),
    path('admi/', views.admi, name='admi'),
    path('logout/', views.logout_view, name='logout'),
    path('change_password/', views.change_password, name='change_password'),
    path('ajou/', views.add_image, name='add_image'),
    path('delete_image/<int:image_id>/', views.delete_image, name='delete_image'),
    path('ajt/', views.ajouter_video, name='ajouter_video'),
    path('supprimer_video/<int:video_id>/', views.supprimer_video, name='supprimer_video'),
    path('ph/', views.photo_list, name='photo_list'),
    path('con/', views.contact, name='contact'),
    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    
    
    
   

    
   
    
    
 
    
    
    
 ]