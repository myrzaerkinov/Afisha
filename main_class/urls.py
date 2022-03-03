from django.urls import path
from . import views

urlpatterns = [
    path('reviews/', views.ReviewListCreateAPIView.as_view()),
    path('reviews/<int:id>/',
         views.ReviewUpdateDeleteAPIView.as_view()),
    path('movies/', views.MoviesListCreateAPIView.as_view()),
    path('movies/<int:id>', views.MoviesUpdateDeleteAPIView.as_view()),
    path('directors/', views.DirectorListCreateAPIView.as_view()),
    path('directors/<int:id>', views.DirectorUpdaterDeleteAPIView.as_view()),
    path('register/', views.RegisterAPIView.as_view())

]