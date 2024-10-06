from django.db import models

class Chefmodel(models.Model):
    Name=models.CharField(max_length=100,null=True)
    Chef=models.CharField(max_length=100,null=True)
    Description=models.CharField(max_length=100,null=True)
    img=models.ImageField(upload_to='Media/pic',null=True)

class Menumodel(models.Model):
    Name=models.CharField(max_length=100,null=True)
    Price=models.CharField(max_length=100,null=True)
    Description=models.CharField(max_length=100,null=True)
    img=models.ImageField(upload_to='Media/pic',null=True)

