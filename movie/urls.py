from movie import views
from django.urls import path


urlpatterns = [
    path(r'movie/', views.MovieList.as_view()),
    path(r'movie/<int:pk>/', views.MovieDetail.as_view())
]