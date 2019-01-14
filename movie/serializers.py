from rest_framework import serializers
from movie.models import Movie, MovieFile


class MovieSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Movie
        fields = '__all__'


class MovieFileSerializer(serializers.ModelSerializer):

    class Meta:
        model = MovieFile
        fields = ('id', 'file', 'folder', 'dateFolderPath', 'fileName')
        read_only_fields = ('folder', 'dateFolderPath', 'fileName')
