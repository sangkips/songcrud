from django.db import models

# Create your models here.


class Artist(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()

    def __str__(self):
        return self.first_name


class Song(models.Model):
    title = models.CharField(max_length=255)
    date_released = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    artist_id = models.ForeignKey(Artist, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title


class Lyric(models.Model):
    content = models.TextField()
    song_id = models.OneToOneField(Song, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

