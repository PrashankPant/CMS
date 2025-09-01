from django.db import models

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(blank=True)
    image = models.ImageField()
    
