# Create your models here.
from django.db import models

# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=100)
    artist_name = models.CharField(max_length=100)
    release_year = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Review(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="reviews")
    author = models.CharField(max_length=100, default="no review author")
    body = models.TextField()

    def __str__(self):
        return self.author
