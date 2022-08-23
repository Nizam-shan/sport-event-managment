from django.db import models
from new_admin.models import Tournaments
from django.contrib.auth.models import User

# Create your models here.
class TournamentApply(models.Model):
    tournament = models.ForeignKey(Tournaments, on_delete=models.CASCADE)
    college = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.tournament} {self.college}"

