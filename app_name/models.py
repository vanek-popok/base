from django.db import models

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=55)
    embed = models.TextField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)