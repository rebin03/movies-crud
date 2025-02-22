from django.db import models

# Create your models here.

class Movie(models.Model):
    
    title = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    genre = models.CharField(max_length=50)
    duration = models.CharField(max_length=10)
    language = models.CharField(max_length=50)
    rating = models.FloatField()
    description = models.TextField()
    poster = models.ImageField(upload_to='images/', null=True, blank=True)
    
    
    def __str__(self):
        return self.title
    
    