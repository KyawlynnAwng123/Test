from django.db import models

# Create your models here.

class Person(models.Model):
    created=models.DateTimeField(auto_now=True)
    name=models.CharField(max_length=100,blank=True,null=True)
    
    def __str__(self):
        return self.name
