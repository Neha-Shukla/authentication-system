from django.db import models
from django.urls import reverse


class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField(max_length=100)

    def get_absolute_url(self):
        return reverse('mysite:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.album_title + ' - ' + self.artist + ' - ' + self.genre + ' - ' + self.album_logo.url


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    audio_file = models.FileField(null=False, blank=True, max_length=10000)
    video = models.CharField(null=True, blank=True, max_length=100)

    def __str__(self):
        return self.song_title
