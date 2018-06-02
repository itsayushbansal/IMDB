from rest_framework import serializers

from .models import *


class GenreSerializer(serializers.ModelSerializer):
    """
    To serialize genre objects data
    """
    class Meta:
        model = Genre
        fields = ('name',)

class MovieSerializer(serializers.ModelSerializer):
    """
    To serialize movie objects data
    """
    genre_ids = serializers.ListField(child=serializers.PrimaryKeyRelatedField(queryset=Genre.objects.filter(is_deleted=False)),
                                      write_only=True,allow_empty=False)
    genre = GenreSerializer(many=True,read_only=True)

    def create(self, validated_data):
        genre_ids = validated_data.pop('genre_ids')
        movie_obj = Movie.objects.create(**validated_data)
        movie_obj.genre.add(*genre_ids)
        return movie_obj

    def update(self, instance, validated_data):
        if validated_data.get('genre_ids'):
            instance.genre.clear()
            instance.genre.add(*validated_data.pop('genre_ids'))
        Movie.objects.filter(id=instance.id).update(**validated_data)
        return instance

    class Meta:
        model = Movie
        fields = '__all__'