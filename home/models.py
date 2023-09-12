from django.db import models

# Create your models here.
class Customer(models.Model):
    username=models.CharField(max_length=20,blank=True)
    mail=models.CharField(max_length=50,blank=True)
    phone=models.CharField(max_length=10,blank=True)
    password=models.CharField(max_length=20)

    def __str__(self) :
        return f"{self.username}"
    