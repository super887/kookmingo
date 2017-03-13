from django.db import models

class Menu(models.Model):
    id=models.AutoField(primary_key=True)
    cafe_name = models.CharField(max_length=30)
    time = models.CharField(max_length=30)
    menu = models.CharField(max_length=3000)


# Create your models here.
