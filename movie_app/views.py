from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie_app.serializer import DirectorSerializer
from movie_app.serializer import MovieSerializer, \
    MovieCreateUpdateSerializer, MovieReadDeleteSerializer, \
    DirectorCreateUpdateSerializer, DirectorReadDeleteSerializer, \
    ReviewCreateUpdateSerializer, ReviewReadDeleteSerializer
from movie_app.serializer import ReviewSerializer
from movie_app.models import Director
from movie_app.models import Movie
from movie_app.models import Review
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


@api_view(['GET', 'POST'])
def directors(request):
    if request.method == 'GET':
        director = Director.objects.all()
        data = DirectorSerializer(director, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        serializer = DirectorCreateUpdateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
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
        serializer = DirectorReadDeleteSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        data = DirectorSerializer(director).data
        return Response(data=data)
    elif request.method == 'DELETE':
        serializer = DirectorReadDeleteSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = DirectorReadDeleteSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
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
    elif request.method == 'POST':
        serializer = MovieCreateUpdateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        title = request.data.get('title')
        description = request.data.get('description')
        duration = request.data.get('duration')
        director = request.data.get('director')
        director_id = request.data.get('director_id')
        movies = Movie.objects.create(title=title, description=description,
                                      director=director, director_id=director_id ,
                                      duration=duration)
        return Response(data=MovieSerializer(movies).data,
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def movies_detail(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'message': 'Movies not found'})
    if request.method == 'GET':
        serializer = MovieReadDeleteSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        data = MovieSerializer(movie, many=False).data
        return Response(data=data)
    elif request.method == 'DELETE':
        serializer = MovieReadDeleteSerializer(data=request.data)
        if not serializer.is_valid():
            movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = MovieReadDeleteSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        movie.title = request.data.get('title')
        movie.description = request.data.get('description')
        movie.duration = request.data.get('duration')
        movie.director = request.data.get('director')
        movie.director_id = request.data.get('director_id')

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
        serializer = ReviewCreateUpdateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        text = request.data.get('text')
        stars = request.data.get('stars')
        movie_id = request.data.get('movie_id')
        review = Review.objects.create(text=text, stars=stars, movie_id=movie_id)
        return Response(data=ReviewSerializer(review).data,
                        status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def reviews_detail(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'message': 'Reviews not found'})
    if request.method == 'GET':
        serializer = ReviewReadDeleteSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        data = ReviewSerializer(review, many=False).data
        return Response(data=data)
    elif request.method == 'DELETE':
        serializer = ReviewReadDeleteSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = ReviewReadDeleteSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        review.text = request.data.get('text')
        review.stars = request.data.get('stars')
        review.save()
        return Response(data=ReviewSerializer(review).data)

##########################################################################
@api_view(['GET'])
def movies_reviews(request):
    print(request.user)
    movies_review = Movie.objects.all()
    data = MovieSerializer(movies_review, many=True).data
    return Response(data=data)



@api_view(['POST'])
def registration(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        User.objects.create_user(username=username, password=password)
        return Response(data={'message': 'User created'},
                        status=status.HTTP_201_CREATED)


@api_view(['POST'])
def authorization(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            try:
                token = Token.objects.get(user=user)
            except Token.DoesNotExist:
                token = Token.objects.create(user=user)
            return Response(data={'key': token.key})

        return Response(data={'error': 'User not found'},
                        status=status.HTTP_404_NOT_FOUND)




