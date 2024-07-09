from django.db import models

# Create your models here.

class Basket(models.Model):
    name = models.CharField(max_length=50)
    rating = models.CharField(max_length=40)
    items = models.PositiveIntegerField()


class Fruit(models.Model):
    name = models.CharField(max_length=40)
    expired_date = models.BooleanField(default=True)
    price = models.PositiveSmallIntegerField()
    
    basket = models.ForeignKey(Basket,on_delete=models.DO_NOTHING,null=True)
    owner = models.ForeignKey('Owner',on_delete=models.DO_NOTHING,null=True)
   

class Owner(models.Model):
    name = models.CharField(max_length=50)
    shop_name = models.CharField(max_length=50)

    #fruit_set
