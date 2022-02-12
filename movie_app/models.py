from django.db import models

class Director(models.Model):
    objects = None
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Movie(models.Model):
    objects = None
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    duration = models.CharField(max_length=200)
    director = models.ForeignKey(Director,
                                 on_delete=models.CASCADE,
                                 related_name="movie")
    def __str__(self):
        return self.director.name

class Review(models.Model):
    objects = None
    text = models.TextField(null=True, blank=True)
    movie = models.ForeignKey(Movie,
                              on_delete=models.CASCADE,
                              related_name="review")

    def __str__(self):
        return self.text

