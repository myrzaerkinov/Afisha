from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie_app.serializer import DirectorSerializer
from movie_app.serializer import MovieSerializer
from movie_app.serializer import ReviewSerializer
from movie_app.models import Director
from movie_app.models import Movie
from movie_app.models import Review
from rest_framework import status

@api_view(['GET', 'POST'])
def directors(request):
    if request.method == 'GET':
        director = Director.objects.all()
        data = DirectorSerializer(director, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        print(request.data)
        name = request.data.get('name')
        director = Director.objects.create(name=name)
        return Response(data=DirectorSerializer(director).data,
                        status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def directors_detail(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'message': 'Director not found'})
    if request.method == 'GET':
        data = DirectorSerializer(director).data
        return Response(data=data)
    elif request.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        director.name = request.data.get('name')
        director.save()
        return Response(data=DirectorSerializer(director).data)
#######################################################################
@api_view(['GET', 'POST'])
def movies(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        data = MovieSerializer(movies, many=True).data
        return Response(data=data)
    elif request.data == 'POST':
        print(request.data)
        title = request.data.get('title')
        description = request.data.get('description')
        duration = request.data.get('duration')
        director = request.data.get('director')
        movie = Movie.objects.create(title=title, description=description,
                                     duration=duration, director=director)
        return Response(data=MovieSerializer(movie).data,
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def movies_detail(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'message': 'Movies not found'})
    if request.method == 'GET':
        data = MovieSerializer(movie, many=False).data
        return Response(data=data)
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        movie.title = request.data.get('title')
        movie.description = request.data.get('description')
        movie.duration = request.data.get('duration')
        movie.director = request.data.get('director')
        movie.save()
        return Response(data=MovieSerializer(movie).data)
########################################################################
@api_view(['GET', 'POST'])
def reviews(request):
    if request.method == 'GET':
        review = Review.objects.all()
        data = ReviewSerializer(review, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        print(request.data)
        text = request.data.get('text')
        stars = request.data.get('stars')
        review = Review.objects.create(text=text, stars=stars)
        return Response(data=ReviewSerializer(review).data,
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'POST'])
def reviews_detail(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'message': 'Reviews not found'})
    if request.method == 'GET':
        data = ReviewSerializer(review, many=False).data
        return Response(data=data)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        review.text = request.data.get('text')
        review.stars = request.data.get('stars')
        review.save()
        return Response(data=ReviewSerializer(review).data)

##########################################################################
@api_view(['GET'])
def movies_reviews(request):
    movies_review = Movie.objects.all()
    data = MovieSerializer(movies_review, many=True).data
    return Response(data=data)
