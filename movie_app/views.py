from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie_app.serializer import AfishaForm
from movie_app.serializer import AfishaForm1
from movie_app.serializer import AfishaForm2
from movie_app.models import Director
from movie_app.models import Movie
from movie_app.models import Review
from rest_framework import status

@api_view(['GET'])
def directors():
    director = Director.objects.all()
    data = AfishaForm(director, many=True).data
    return Response(data=data)


@api_view(['GET'])
def directors_detail(id):
    try:
        director = Director.objects.get(id=id)
    except Director:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'message': 'Director not found'})
    data = AfishaForm(director, many=False).data
    return Response(data=data)

@api_view(['GET'])
def movies():
    movie = Movie.objects.all()
    data = AfishaForm1(movie, many=True).data
    return Response(data=data)

@api_view(['GET'])
def movies_detail(id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'message': 'Movies not found'})
    data = AfishaForm1(movie, many=False).data
    return Response(data=data)

@api_view(['GET'])
def reviews():
    review = Review.objects.all()
    data = AfishaForm2(review, many=True).data
    return Response(data=data)


@api_view(['GET'])
def reviews_detail(id):
    try:
        review = Review.objects.get(id=id)
    except Review:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'message': 'Reviews not found'})
    data = AfishaForm2(review, many=False).data
    return Response(data=data)


