from rest_framework import serializers
from movie_app.models import Movie
from movie_app.models import Review
from movie_app.models import Director

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    reviews = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = 'id title all_reviews reviews rating '.split()

    def get_reviews(self, movie):
        serializer = ReviewSerializer(Review.objects.filter(movie=movie), many=True)
        return serializer.data

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"



