from django.db import models
from bs4 import BeautifulSoup
from urllib.request import urlopen

class Menu(models.Model):
    id=models.AutoField(primary_key=True)
    cafe_name = models.CharField(max_length=30,default="")
    time = models.CharField(max_length=30,default="")
    menu = models.CharField(max_length=100,default="")


# Create your models here.
