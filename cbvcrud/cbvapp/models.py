from django.db import models
from django.urls import reverse
class Students(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    score = models.IntegerField()
    
    def __str__(self):
        return self.firstname
    def get_absolute_url(self):
        return reverse("detail", kwargs= {"pk" : self.pk})
