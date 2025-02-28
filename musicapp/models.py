from django.db import models
from PIL import Image

def user_path(instance, filename):
    return f'uploads/{instance.artist.id}/{filename}'

class User(models.Model):
    userID = models.IntegerField(
        verbose_name='ユーザID',
    )
    user_name = models.CharField(
        verbose_name='ユーザ名',
        max_length=25
    )
    email = models.EmailField(
        verbose_name='メールアドレス',
        max_length=256,
        unique=True
    )
    password = models.CharField(
        verbose_name='パスワード',
        max_length=100
    )

    def __int__(self):
        return self.userID

class Artist(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(default="No bio available")
    profile_image = models.ImageField(upload_to='artists/profile_images/', default='path/to/default/profile_image.jpg')
    background_image = models.ImageField(upload_to='artists/background_images/', default='path/to/default/background_image.jpg')
    twitter_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    facebook_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, related_name='songs', on_delete=models.CASCADE)
    file = models.FileField(upload_to=user_path, verbose_name='曲ファイル', default='songs/default_song.mp3')

    def __str__(self):
        return self.title