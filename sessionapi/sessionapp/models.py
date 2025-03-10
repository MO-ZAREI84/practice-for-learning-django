from django.db import models

class Addmodel(models.Model):
    name = models.CharField(max_length=50)
    quntity = models.CharField(max_length=50)