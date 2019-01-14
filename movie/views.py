from movie.models import Movie, MovieFile
from movie.serializers import MovieSerializer, MovieFileSerializer
from rest_framework import generics
from rest_framework import permissions
from movie.permissions import IsOwnerOrReadOnly
import os
import datetime
from django.conf import settings
import hashlib
from rest_framework.response import Response
from rest_framework import status


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

    def post(self, request, *args, **kwargs):

        uploaded_file = request.FILES['file']
        if uploaded_file is not None:

            directory = os.path.dirname(os.path.abspath(__file__)) + "/.." + settings.MEDIA_URL + datetime.datetime.today().strftime('%Y-%m-%d')

            if not os.path.exists(directory):
                os.makedirs(directory)

            fileName = hashlib.md5(uploaded_file.name.encode()).hexdigest()
            fileExtention = os.path.splitext(str(request.FILES['file']))[1].replace(".", "")
            fileName = fileName +"."+ fileExtention
            with open(directory + "/" + fileName, 'wb+') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)
                    destination.close()

            request.data["fileName"] = fileName
            request.data["dateFolderPath"] = settings.MEDIA_URL
            request.data["folder"] = settings.MEDIA_URL

        serializer = MovieFileSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        serializer.save()

        return Response(serializer.data, status.HTTP_200_OK)


class FileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MovieFile.objects.all()
    serializer_class = MovieFileSerializer
    permission_classes = (IsOwnerOrReadOnly,)
