from django import forms
from .models import Song
from .models import Artist

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'artist', 'file']

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['name', 'bio', 'profile_image', 'background_image', 'twitter_url', 'instagram_url', 'facebook_url']