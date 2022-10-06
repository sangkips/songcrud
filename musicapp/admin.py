from django.contrib import admin
from .models import Lyric, Artist, Song

# Register your models here.

admin.site.register([Lyric, Song, Artist])
