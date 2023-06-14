from django.db import models
from django.urls import reverse

# Create your models here.

class School(models.Model):
    name=models.CharField(max_length=20)
    principal=models.CharField(max_length=40)
    location=models.CharField(max_length=30)
    def __str__(self):
        return self.name
    

    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})

class Students(models.Model):
    school=models.ForeignKey(School,on_delete=models.CASCADE,related_name='Students')
    sname=models.CharField(max_length=20)
    sage=models.IntegerField()

    def __str__(self):
        return self.sname
    
    