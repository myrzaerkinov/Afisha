from django.contrib import admin
from django.urls import path, include
from movie_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/directors/', views.directors),
    path('api/v1/directors/<int:id>/', views.directors_detail),
    path('api/v1/movies/', views.movies),
    path('api/v1/movies/<int:id>/', views.movies_detail),
    path('api/v1/reviews/', views.reviews),
    path('api/v1/reviews/<int:id>/', views.reviews_detail),
    path('api/v1/movies/reviews/', views.movies_reviews),
    path('api/v1/register/', views.registration),
    path('api/v1/login/', views.authorization),
    path('api/v1/cbv/', include('main_class.urls'))

]
