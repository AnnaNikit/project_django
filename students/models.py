from django.db import models
from re import *
import datetime
# Create your models here.
class Student(models.Model):
    name       = models.CharField(max_length=255)
    surname    = models.CharField(max_length=255)
    email      = models.EmailField(max_length=255,blank=True, unique=True)
    phone      = models.CharField(max_length=255)
    start_date = models.DateField()

    def __str__(self):
            return '%s %s'%(self.surname,self.name)

    def is_valid(self):
        pattern = compile('(^|\s)[-a-z0-9_.]+@([-a-z0-9]+\.)+[a-z]{2,6}(\s|$)')
        email_is_valid = pattern.match(self.email)
        messege = ''
        if email_is_valid == None:
           messege = 'Please enter a real email\n'

        if not self.name.isalpha() or len(self.name)<=3:
           messege = messege +"Please enter a real name"

        if len(messege)  == 0:
             return True
        else:
             return messege
