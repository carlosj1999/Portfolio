from django.db import models

# Create your models here.
class Resume(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)