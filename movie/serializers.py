from rest_framework import serializers
from movie.models import Movie, MovieFile, Classification


class MovieFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieFile
        fields = '__all__'


class ClassificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Classification
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    classification = ClassificationSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ('id', 'title', 'desc', 'owner', 'file_id', 'classification')
