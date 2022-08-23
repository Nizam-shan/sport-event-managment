from django.db import models
from django.contrib.auth.models import User


class Tournaments(models.Model):
    category = (
        ('male','Male'),
        ('Female','Female'),
        ('Both','Both'),
    )
    college = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey('Event', on_delete=models.CASCADE)
    category = models.CharField(choices=category, max_length=10)
    date = models.DateField(null=True, blank=True)
    level = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.event.name}  {self.college.username}'


class Event(models.Model):
    name = models.CharField(max_length=50)
    players = models.IntegerField()

    def __str__(self):
        return self.name


class Winner(models.Model):
    tournament = models.ForeignKey(Tournaments, on_delete=models.CASCADE)
    winner = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.tournament} {self.winner}'