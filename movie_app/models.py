from django.db import models
from django.db.models import Avg

class Director(models.Model):
    objects = None
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    @property
    def all_movies(self):
        movies = Movie.objects.filter(movie=self)
        return [{'id': i.id, 'text': i.text} for i in movies]


class Movie(models.Model):
    objects = None
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True, blank=True)
    duration = models.CharField(max_length=200)
    director = models.ForeignKey(Director,
                                 on_delete=models.CASCADE,
                                 related_name="movie")
    def __str__(self):
        return self.director.name

    @property
    def rating(self):
        # return Review.objects.filter(movie_id=self).aggregate(Avg('stars'))

        reviews = Review.objects.filter(movie=self)
        sum_ = 0
        for i in reviews:
            sum_ += int(i.stars)
        try:
            return sum_/reviews.count()
        except:
            return 0

    @property
    def all_movies(self):
        movies = Movie.objects.filter(movie=self)
        return [{'id': i.id, 'text': i.text} for i in movies]

    @property
    def all_reviews(self):
        reviews = Review.objects.filter(movie=self)
        return [{'id': i.id, 'text': i.text} for i in reviews]

class Review(models.Model):
    RATING_REVIEW = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    )
    objects = None
    text = models.TextField(null=True, blank=True)
    movie = models.ForeignKey(Movie,
                              on_delete=models.CASCADE,
                              related_name="review")
    stars = models.CharField(choices=RATING_REVIEW,
                             max_length=100,
                             null=True, blank=True)
    def __str__(self):
        return self.text

