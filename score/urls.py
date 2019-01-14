from score import views
from django.urls import path


urlpatterns = [
    path(r'', views.ScoreList.as_view()),
    path(r'<int:pk>/', views.ScoreDetail.as_view())
]