from django.shortcuts import render
from django.views import generic
from .models import Album, Song
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django import forms
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import UserRegistrationForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    return render(request, 'mysite/home.html')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email = userObj['email']
            password = userObj['password']
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password)
                user = authenticate(username=username, password=password)
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                raise forms.ValidationError('Looks like a username with that email or password already exists')
    else:
        form = UserRegistrationForm()
    return render(request, 'mysite/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'mysite/profile.html')


class IndexView(generic.ListView):
    template_name = 'mysite/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()


class DetailView(generic.DetailView):
    model = Album
    template_name = 'mysite/detail.html'


class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']


class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']


class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('mysite:index')


class SongCreate(CreateView):
    model = Song
    fields = ['album', 'file_type', 'song_title', 'audio_file', 'video']
    success_url = reverse_lazy('mysite:index')


class SongView(generic.ListView):
    template_name = 'mysite/songs.html'
    context_object_name = 'all_songs'

    def get_queryset(self):
        return Song.objects.all()



