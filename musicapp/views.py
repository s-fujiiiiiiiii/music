from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import User, Artist
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Song
from .forms import SongForm
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.views import LoginView
from django.db.models import Q
from django.views.generic import ListView
from .models import User, Song, Artist
from django.shortcuts import redirect
from .models import Artist
from .forms import ArtistForm
from django.shortcuts import render, get_object_or_404
from django.views import View

class IndexView(ListView):
    template_name = 'home.html'
    model = Artist
    context_object_name = 'artists'
    queryset = Artist.objects.order_by('id')


class SearchView(ListView):
    template_name = 'search.html'
    context_object_name = 'results'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            user_results = User.objects.filter(Q(user_name__icontains=query) | Q(email__icontains=query))
            song_results = Song.objects.filter(Q(title__icontains=query) | Q(artist__name__icontains=query))
            artist_results = Artist.objects.filter(name__icontains=query)
            results = list(user_results) + list(song_results) + list(artist_results)
            
            return results
        return []


class ArtistListView(ListView):
    model = Artist
    template_name = 'artist_list.html'
    context_object_name = 'artists'
    queryset = Artist.objects.order_by('id')

class ArtistDetailView(DetailView):
    model = Artist
    template_name = 'artist_detail.html'
    context_object_name = 'artist'

class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff

class SongUploadView(AdminRequiredMixin, CreateView):
    model = Song
    form_class = SongForm
    template_name = 'upload_song.html'
    success_url = reverse_lazy('song_list')

class CustomLoginView(LoginView):
    template_name = 'musicapp/login.html'

class UserLoginView(LoginView):
    template_name = 'login.html'

class SongDetailView(DetailView):
    model = Song
    template_name = 'song_detail.html'
    context_object_name = 'song'

class ArtistCreateView(CreateView):
    model = Artist
    form_class = ArtistForm
    template_name = 'upload_artist.html'
    success_url = reverse_lazy('artist_list')

    def form_valid(self, form):
        form.instance.profile_image = self.request.FILES.get('profile_image')
        form.instance.background_image = self.request.FILES.get('background_image')
        return super().form_valid(form)
    
class SongPlaybackView(View):
    def get(self, request, pk):
        song = get_object_or_404(Song, pk=pk)
        return render(request, 'musicapp/song_playback.html', {'song': song})
    
class SongPlaybackView(View):
    def get(self, request, pk):
        song = get_object_or_404(Song, pk=pk)
        return render(request, 'musicapp/song_playback.html', {'song': song})