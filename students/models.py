from django.db import models

# Create your models here.
class Student(models.Model):
    name       = models.CharField(max_length=255)
    surname    = models.CharField(max_length=255)
    email      = models.CharField(max_length=255)
    phone      = models.CharField(max_length=255)
    start_date = models.DateField()
    birthday   = models.DateField()

    def __str__(self):
            return '%s %s'%(self.surname,self.name) 
