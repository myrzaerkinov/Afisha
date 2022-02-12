from django.contrib import admin
from django.urls import path
from movie_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/directors/', views.directors),
    path('api/v1/directors/<int:id>/', views.directors_detail),
    path('api/v1/movies/', views.movies),
    path('api/v1/movies/<int:id>/', views.movies_detail),
    path('api/v1/reviews/', views.reviews),
    path('api/v1/reviews/<int:id>/', views.reviews_detail),
]
