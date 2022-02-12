from rest_framework import serializers
from movie_app.models import Movie
from movie_app.models import Review
from movie_app.models import Director

class AfishaForm(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = "__all__"

class AfishaForm1(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"

class AfishaForm2(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"



