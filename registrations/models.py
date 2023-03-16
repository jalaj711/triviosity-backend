from django.db import models

# Create your models here.
class Reverberate(models.Model):
    email = models.EmailField("email", null=False, blank=False)
    name = models.CharField(max_length=200, blank=False)
    number = models.CharField(max_length=20, blank=False)
    roll_no = models.CharField(max_length=10, blank=False)
    section = models.CharField(max_length=10, blank=False)
    hallno = models.CharField(max_length=20, blank=False, default="unknown")

# Create your models here.
class DebReverberate(models.Model):
    email = models.EmailField("email", null=False, blank=False)
    name = models.CharField(max_length=200, blank=False)
    number = models.CharField(max_length=20, blank=False)
    roll_no = models.CharField(max_length=10, blank=False)
    section = models.CharField(max_length=10, blank=False)
    teamname = models.CharField(max_length=10, default="")
    hallno = models.CharField(max_length=20, blank=False, default="unknown")