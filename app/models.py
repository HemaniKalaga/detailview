from django.db import models
from django.urls import reverse
# Create your models here.
class School(models.Model):
    sname=models.CharField(max_length=100,primary_key=True)
    sprincipal=models.CharField(max_length=100)
    slocation=models.CharField(max_length=100)

    #it is a special method.
    #it is used to create dynamic URL mapping(or) Canonical URL mapping

    def get_absolute_url(self):
        return reverse('SchoolDetail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.sname
    
class Student(models.Model):
    stname=models.CharField(max_length=100,primary_key=True)
    stage=models.IntegerField()
    sname=models.ForeignKey(School,on_delete=models.CASCADE,related_name='students')
    def __str__(self):
        return self.stname
    