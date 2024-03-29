from django.db import models
# Create your models here.

class Book(models.Model):
    title= models.CharField(max_length=30,null=False)
    authors=models.CharField(max_length=40,null=False)
    publication_date = models.DateField(null=True,blank=True)
    isbn = models.CharField(max_length=13,null=False,unique=True)
    description=models.TextField(null=True,blank=True)
    
    def __str__(self):
        return self.title