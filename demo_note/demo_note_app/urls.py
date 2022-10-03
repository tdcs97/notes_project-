
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('index/', views.index),
    path('register/', views.register),
    path('user_login/', views.user_login, name='user_login'),
    path('userpage/', views.task, name='userpage'),
    path('user_logout/', views.userlogout, name='user_logout'),
    path('delete_note/<str:myid>/', views.delete_note, name='delete_note'),
    path('edit_note/<int:myid>/', views.edit_note, name='edit_note'),
    path('update_note/<int:myid>/', views.update_note, name='update_note'),
    path('search/', views.search, name='search'),
    path('contact/', views.contact, name='contact'),
    path('aboutus/', views.aboutus, name='aboutus'),
]