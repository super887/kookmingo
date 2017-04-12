from django.db import models

class Menu(models.Model):
    id=models.AutoField(primary_key=True)
    cafe_name = models.CharField(max_length=30)
    time = models.CharField(max_length=30)
    menu = models.TextField(max_length=2000)

    def __str__(self):
        return self.menu


# Create your models here.
