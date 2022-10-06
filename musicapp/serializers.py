from . models import  Song, Artist, Lyric
from rest_framework import serializers

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['title', 'likes', 'date_released']


class LyricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lyric
        fields = '__all__'