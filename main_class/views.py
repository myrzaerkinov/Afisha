from rest_framework.generics import ListAPIView, \
    ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView
from movie_app.models import Review, Movie, Director
from movie_app.serializer import ReviewSerializer,\
    MovieSerializer,\
    DirectorSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView

# # # # # # # #
class ReviewListCreateAPIView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = PageNumberPagination
    filter_fields = ['stars']

class ReviewUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = 'id'
# # # # # # # #
class MoviesListCreateAPIView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = PageNumberPagination
    filter_fields = ['title']

class MoviesUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = 'id'
# # # # # # # #
class DirectorListCreateAPIView(ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    pagination_class = PageNumberPagination
    filter_fields = ['name']

class DirectorUpdaterDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    lookup_field = 'id'
# # # # # # # #
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserCreateSerializer
from rest_framework.permissions import IsAuthenticated

class RegisterAPIView(GenericAPIView):
    serializer_class = UserCreateSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        User.objects.create_user(**serializer.validated_data)
        return Response(data={'message': 'Пользователь зарегистрирован !'},
                        status=status.HTTP_201_CREATED)
# # # # # # # #







