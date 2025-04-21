from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20)
    department = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Staff(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.name
