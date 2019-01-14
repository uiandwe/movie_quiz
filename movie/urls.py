from movie import views
from django.urls import path


urlpatterns = [
    path(r'', views.MovieList.as_view()),
    path(r'<int:pk>/', views.MovieDetail.as_view()),
    path(r'file/', views.FileList.as_view()),
    path(r'file/<int:pk>/', views.FileDetail.as_view())
]