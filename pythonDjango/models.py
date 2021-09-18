from django.db import models

# Create your models here.
class Contact(models.Model):
    email=models.CharField( max_length=100)
    password=models.CharField(max_length=18)
    name=models.CharField(max_length=150)
    address=models.TextField(max_length=500)
    product=models.CharField(max_length=5)
    date=models.DateField()
    def __str__(self):
        return self.name
        