from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)

class MenuItem(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)




