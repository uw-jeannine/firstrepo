from django.db import models

# Create your models here.
class Registration(models.Model):
    phone =models.CharField(max_length=255)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    def __str__(self):
        return self.firstname


class Student(models.Model):
    firstname = models.CharField(max_length=255)
    lastname  = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    age = models.CharField(max_length=255)
    