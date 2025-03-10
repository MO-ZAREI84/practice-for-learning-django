from django.db import models

class Students(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    numeric = models.IntegerField()
