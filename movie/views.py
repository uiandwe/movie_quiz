from movie.models import Movie, MovieFile, Classification
from movie.serializers import MovieSerializer, MovieFileSerializer, ClassificationSerializer
from rest_framework import generics
from rest_framework import permissions
from movie.permissions import IsOwnerOrReadOnly


class MovieList(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class FileList(generics.ListCreateAPIView):
    queryset = MovieFile.objects.all()
    serializer_class = MovieFileSerializer

    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class FileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MovieFile.objects.all()
    serializer_class = MovieFileSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class ClassificationList(generics.ListCreateAPIView):
    queryset = Classification.objects.all()
    serializer_class = ClassificationSerializer


class ClassificationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Classification.objects.all()
    serializer_class = ClassificationSerializer
