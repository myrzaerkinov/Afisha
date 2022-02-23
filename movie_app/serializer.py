from rest_framework import serializers
from movie_app.models import Movie
from movie_app.models import Review
from movie_app.models import Director
from rest_framework.exceptions import ValidationError
###################################################################################

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'

class DirectorCreateUpdateSerializer(serializers.Serializer):
    name = serializers.CharField(min_length=6, max_length=10)

class DirectorReadDeleteSerializer(serializers.Serializer):
    name = serializers.CharField(min_length=6, max_length=10)
###################################################################################

class MovieSerializer(serializers.ModelSerializer):
    reviews = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = 'id title all_reviews reviews rating '.split()

    def get_reviews(self, movie):
        serializer = ReviewSerializer(Review.objects.filter(movie=movie), many=True)
        return serializer.data

class MovieCreateUpdateSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=6, max_length=16)
    description = serializers.CharField()
    duration = serializers.CharField(max_length=30)
    director_id = serializers.CharField()

class MovieReadDeleteSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=6, max_length=16)
    description = serializers.CharField()
    duration = serializers.CharField(max_length=30)
    director_id = serializers.CharField()
###################################################################################
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"

class ReviewCreateUpdateSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=10, min_length=5)
    stars = serializers.IntegerField(min_value=1, max_value=5)
    movie_id = serializers.IntegerField()

class ReviewReadDeleteSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=10, min_length=5)
    stars = serializers.IntegerField(min_value=1, max_value=5)
    movie_id = serializers.IntegerField()
