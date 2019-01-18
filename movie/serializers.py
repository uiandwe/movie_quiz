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

    class Meta:
        model = Movie
        fields = ('id', 'title', 'desc', 'owner', 'file_id')
        # depth = 1 #해당 옵션시 리스트엔 객체로 보이지만 post를 날릴수 없음
