from django.db import models

class products(models.Model):
    title=models.CharField(max_length=200,blank=False)
    price=models.IntegerField()
    category=models.CharField(max_length=40,blank=False)
    desc=models.TextField(blank=False)
    image= models.FileField(upload_to='Images/',max_length=250,null=True,default=None)
class user_cred(models.Model):
    name=models.CharField(max_length=40)
    email=models.EmailField()
    phone=models.CharField(max_length=10)
    password=models.CharField(max_length=100)

class card(models.Model):
    productId=models.IntegerField()
    email=models.EmailField()
    title=models.CharField(max_length=150)
    desc=models.CharField(max_length=500)
    category=models.CharField(max_length=100)
    image=models.URLField()
    price=models.FloatField()

class address(models.Model):
   
    email=models.EmailField()
    name=models.CharField(max_length=150)
    phone=models.IntegerField()
    pin=models.IntegerField()
    locality=models.CharField(max_length=100)
    add=models.CharField(max_length=200)

