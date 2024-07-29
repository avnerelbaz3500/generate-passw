from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator 



# Create your models here.
class Generate(models.Model):
   
    
    mdp =  models.fields.CharField(null = True ,max_length=100,blank=True)
    special = models.fields.BooleanField(default=True, verbose_name= "Caractères spéciaux ")
    simple = models.fields.BooleanField(default=False, verbose_name= "Mot de Passe Simple à retenir ")
    scale = models.fields.IntegerField(null =True, default= 8, blank=True)
    password = models.fields.CharField(null = True, max_length=128, blank=True)
    passphrase = models.fields.CharField(null = True, max_length=1000, blank=True)
    passphrase_created = models.fields.CharField(null = True, max_length=128, blank=True)
    dico_scale = models.fields.IntegerField(null =True, default= 4, blank=True)
    passmot = models.fields.CharField(null = True, max_length=128,blank=True)
    separator = models.fields.CharField(default='/', max_length=3)






    


   
    







