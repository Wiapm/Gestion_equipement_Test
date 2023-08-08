
from django.urls import path
from . import views
urlpatterns = [
    path('',views.accueil_visiteur , name='accueil_visiteur'),
    path('search/', views.search_equipments2, name='search_equipments2'), 
    path('contact_laboratoire/<int:equipement_id>/', views.contact_laboratoire, name='contact_laboratoire'),
    path('liste_messages_reservation/', views.liste_messages_reservation, name='liste_messages_reservation'),
    path('mon_compte/', views.my_account, name='my_account'),
    path('delete_account/', views.delete_account, name='delete_account'),
    path('supprimer-message/', views.supprimer_message_reservation, name='supprimer_message_reservation'),
    
]
