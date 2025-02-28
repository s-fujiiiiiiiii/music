from django.urls import path
from .views import IndexView, UserLoginView, SearchView, ArtistListView, ArtistDetailView, SongUploadView, SongDetailView, ArtistCreateView
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path
from .views import IndexView, UserLoginView, SearchView, ArtistListView, ArtistDetailView, SongUploadView, SongDetailView, ArtistCreateView, SongPlaybackView

app_name = 'musicapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('search/', SearchView.as_view(), name='search'),
    path('artists/', ArtistListView.as_view(), name='artist_list'),
    path('artists/<int:pk>/', ArtistDetailView.as_view(), name='artist_detail'),
    path('songs/<int:pk>/', SongDetailView.as_view(), name='song_detail'),
    path('upload/', SongUploadView.as_view(), name='upload_song'),
    path('artists/create/', ArtistCreateView.as_view(), name='create_artist'),
    path('song/<int:pk>/', SongPlaybackView.as_view(), name='song_playback'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)