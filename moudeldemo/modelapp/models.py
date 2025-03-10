from django.db import models

class student(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    salary = models.FloatField(max_length=30)
    email = models.EmailField()