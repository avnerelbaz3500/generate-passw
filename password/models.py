from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator





# Create your models here.
class Generate(models.Model):
   
    
    mdp =  models.fields.CharField(null = True ,max_length=100)
    special = models.fields.BooleanField(default=True, verbose_name= "Caractères spéciaux ")
    simple = models.fields.BooleanField(default=False, verbose_name= "Mot de Passe Simple à retenir ")
    scale = models.fields.IntegerField(null =True, default= 8)
    password = models.fields.CharField(null = True, max_length=128)
    passphrase = models.fields.CharField(null = True, max_length=1000)
    passphrase_created = models.fields.CharField(null = True, max_length=128)
    dico_scale = models.fields.IntegerField(null =True, default= 4)






    


   
    







