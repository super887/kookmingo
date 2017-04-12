from django.db import models

class Hanul(models.Model):
    id=models.AutoField(primary_key=True)
    cafe_name = models.CharField(max_length=30)
    time = models.CharField(max_length=30)
    menu = models.TextField(max_length=2000)

    def __str__(self):
        return self.menu


class Student(models.Model):
    id=models.AutoField(primary_key=True)
    cafe_name = models.CharField(max_length=30)
    time = models.CharField(max_length=30)
    menu = models.TextField(max_length=2000)

    def __str__(self):
        return self.menu


class Staff(models.Model):
    id=models.AutoField(primary_key=True)
    cafe_name = models.CharField(max_length=30)
    time = models.CharField(max_length=30)
    menu = models.TextField(max_length=2000)

    def __str__(self):
        return self.menu


class Smell(models.Model):
    id=models.AutoField(primary_key=True)
    cafe_name = models.CharField(max_length=30)
    time = models.CharField(max_length=30)
    menu = models.TextField(max_length=2000)

    def __str__(self):
        return self.menu


class DormitoryNormal(models.Model):
    id=models.AutoField(primary_key=True)
    cafe_name = models.CharField(max_length=30)
    time = models.CharField(max_length=30)
    menu = models.TextField(max_length=2000)

    def __str__(self):
        return self.menu


class DormitoryRoutine(models.Model):
    id=models.AutoField(primary_key=True)
    cafe_name = models.CharField(max_length=30)
    time = models.CharField(max_length=30)
    menu = models.TextField(max_length=2000)


    def __str__(self):
        return self.menu

# Create your models here.
