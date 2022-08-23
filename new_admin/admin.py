from django.contrib import admin
from . models import Event, Tournaments, Winner

admin.site.register(Event)
admin.site.register(Tournaments)
admin.site.register(Winner)

