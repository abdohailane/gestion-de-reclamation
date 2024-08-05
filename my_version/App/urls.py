from django.urls import path
from . import views
from .views import user_list,AddUser,EditUser,DeleteUser,ViewUser,MiseeditUser,miseDelete

urlpatterns = [
    path('principal/', views.princip, name='princip'), 
    path('login/', views.user_login, name='login'),
    path('Reclam/', views.user_reclamation, name='user_reclamation'),
    path('', views.user_list, name='user_list'),
    path('Mise/', views.mise, name='mise'),
    path('Add/', views.AddUser, name='AddUser'),
    path('MiseAdd/', views.Mise_add, name='Mise_add'),
    path('Edit/<int:id>/', views.EditUser, name='EditUser'),
    path('Editmise/<int:id>/', views.MiseeditUser, name='MiseeditUser'),
    path('Delete/<int:eid>/', views.DeleteUser, name='DeleteUser'),
    path('Deletemi/<int:eid>/', views.miseDelete, name='miseDelete'),
    path('View/<int:eid>/', views.ViewUser, name='ViewUser'),
    path('ViewA/<int:eid>/', views.Viewadmin, name='ViewUser'),
    path('reponse/<int:id>/', views.addreponse, name='ViewUser'),
    path('chat/<int:user_id>/', views.chat_view, name='chat_view'),
    path('chatuser/<int:user_id>/', views.chat_view_user, name='chat_view_user'),




    
]
