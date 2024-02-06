from django.db import models

# Create your models here.

class user(models.Model):
    email = models.EmailField( default =None)
    name = models.CharField(max_length =255)
    password = models.CharField(max_length = 255  , default= None)
    age = models.CharField(max_length =255 , null = True , default = None)
    phone = models.CharField(max_length =255 , null =True , default = None)

    def __str__(self) -> str:
        return f"{self.email}"