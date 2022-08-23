from . import views
from django.urls import path

urlpatterns = [
    path('',views.admin_home, name='adminhome'),
    path('adminlogin',views.admin_login, name='adminlogin'),
    path('adminlogout',views.admin_logout, name='adminlogout'),
    path('addcollege',views.add_college, name='addcollege'),
    path('colleges',views.colleges, name='colleges'),
    path('tournaments',views.tournaments, name='tournaments'),
    path('addevents',views.addevents, name='addevents'),
    path('addwinner',views.addwinner, name='addwinner'),
]