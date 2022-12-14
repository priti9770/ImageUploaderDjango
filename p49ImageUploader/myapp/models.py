from django.db import models

# Create your models here.

# class User(models.Model):
#     user_name=models.CharField(max_length=70)
#     password=models.CharField(max_length=70)

class Image(models.Model):
    photos = models.ImageField(upload_to="images")
    date = models.DateTimeField(auto_now_add=True)
    
    
    