from django.db import models

# Create your models here.


class user(models.Model):

   Full_name =models.CharField(max_length=50)
   User_namme =models.CharField(max_length=50)
   Email=models.EmailField(max_length=200)
   Phone=models.CharField(max_length=50)
   Password =models.CharField(max_length=50)
   Confrim_password =models.CharField(max_length=50)

   def __str__(self):
       return self.name
   


