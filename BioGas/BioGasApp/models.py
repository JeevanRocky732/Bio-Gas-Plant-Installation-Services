from django.db import models

# Create your models here.
class Contact(models.Model):
        name = models.CharField(max_length=122)
        email = models.CharField(max_length=122)
        phone = models.CharField(max_length=12)
        desc = models.TextField()
        date = models.DateField()

class Services(models.Model):
        name = models.CharField(max_length=122)
        email = models.CharField(max_length=122)
        password = models.CharField(max_length=122)
        number = models.CharField(max_length=12)
        address = models.CharField(max_length=222)
        date = models.DateField()