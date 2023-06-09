from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=30)
    theme_pic = models.FileField(upload_to="themes/", blank=True, null=True)
    start_time = models.DateTimeField(verbose_name="Start time of the theme:")
    end_time = models.DateTimeField(verbose_name="End time of the theme: ")
    def __str__(self):
        return self.name

class Question(models.Model):
    text = models.TextField()
    clue = models.TextField(default='', blank=True, null=True)
    clue_wait_time = models.IntegerField(default=5)
    round = models.AutoField(primary_key=True)
    genre_round = models.IntegerField(default=1)
    answer = models.CharField(max_length=100)
    media = models.FileField(upload_to="questions/", blank=True, null=True)
    points = models.IntegerField(default=10)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.text

class User(AbstractUser):
    current_round_overall = models.IntegerField(default=1)
    current_genre_round = models.IntegerField(default=1)
    current_genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    current_standings = models.TextField(verbose_name="Standings in different rounds", max_length=400, default="{}")
    points = models.IntegerField(default=0)
    time = models.DateTimeField(auto_now_add=True)
    calc_wait_time_from = models.DateTimeField(blank=True, null=True)
    picture = models.URLField(verbose_name="Avatar of the user: ", default=None, null=True)
    def __str__(self):
        return self.first_name + " " + self.last_name

class Meta(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
