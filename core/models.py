from django.db import models

# Create your models here.

class UserModel(models.Model):
    email = models.EmailField( default =None)
    first_name = models.CharField(max_length =255 , default = None)
    last_name = models.CharField(max_length =255 , default = None)
    password = models.CharField(max_length = 255  , default= None)


    def __str__(self) -> str:
        return f"{self.email}"