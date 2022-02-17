from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie_app.serializer import DirectorSerializer
from movie_app.serializer import MovieSerializer
from movie_app.serializer import ReviewSerializer
from movie_app.models import Director
from movie_app.models import Movie
from movie_app.models import Review
from rest_framework import status

@api_view(['GET'])
def directors(request):
    director = Director.objects.all()
    data = DirectorSerializer(director, many=True).data
    return Response(data=data)

@api_view(['GET'])
def directors_detail(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'message': 'Director not found'})
    data = DirectorSerializer(director, many=False).data
    return Response(data=data)

@api_view(['GET'])
def movies(request):
    movie = Movie.objects.all()
    data = MovieSerializer(movie, many=True).data
    return Response(data=data)

@api_view(['GET'])
def movies_detail(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'message': 'Movies not found'})
    data = MovieSerializer(movie, many=False).data
    return Response(data=data)

@api_view(['GET'])
def reviews(request):
    review = Review.objects.all()
    data = ReviewSerializer(review, many=True).data
    return Response(data=data)

@api_view(['GET'])
def reviews_detail(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'message': 'Reviews not found'})
    data = ReviewSerializer(review, many=False).data
    return Response(data=data)

@api_view(['GET'])
def movies_reviews(request):
    movies_review = Movie.objects.all()
    data = MovieSerializer(movies_review, many=True).data
    return Response(data=data)



