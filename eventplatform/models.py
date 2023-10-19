from django.db import models

class user(models.Model):
    username=models.CharField(max_length=255)
    email=models.EmailField()
    password1=models.CharField(max_length=255)

class log(models.Model):
    signins =models.BooleanField()
    username = models.CharField(max_length=255)
    emailid = models.EmailField()  

class fund(models.Model):
    user=models.CharField(max_length=255)
    username=models.CharField(max_length=255)
    goal=models.IntegerField()
    message=models.CharField(max_length=255)
    image=models.ImageField(upload_to="images/")
