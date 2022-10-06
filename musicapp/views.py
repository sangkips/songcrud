from django.shortcuts import render
from rest_framework import status, viewsets
from .serializers import ArtistSerializer, LyricsSerializer, SongSerializer
from .models import Artist, Song, Lyric


# Create your views here.
class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class LyricViewSet(viewsets.ModelViewSet):
    queryset = Lyric.objects.all()
    serializer_class = LyricsSerializer





