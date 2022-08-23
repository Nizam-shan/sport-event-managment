from . import views
from django.urls import path

urlpatterns = [
    path('',views.index, name='index'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('gallery',views.gallery,name='gallery'),
    path('home',views.home, name='home'),
    path('login',views.admin_login, name='login'),
    path('logout',views.admin_logout, name='logout'),
    path('addtournament',views.add_tournament, name='addtournament'),
    path('tournament',views.tournament, name='tournament'),
    path('results',views.results, name='results'),
    path('apply/<int:id>',views.apply, name='apply'),       
]