from django.db import models

# Create your models here.

class Employee(models.Model):
    id = models.BigAutoField(primary_key=True)
    name =  models.CharField(max_length = 200 ,blank=True,null=True)
    age = models.IntegerField(null=True,blank=True)
    
    def __str__(self):
        return f'{self.id}'
