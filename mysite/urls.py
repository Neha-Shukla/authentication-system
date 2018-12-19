from django.conf.urls import url, include
from django.contrib import admin
from . import views
from .views import home, register

app_name = 'mysite'

urlpatterns = [

    url(r'^register/', register, name='register'),
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /music/album_id/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # /music/album/add
    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),

    # /music/album/album_id/update
    url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),

    # /music/album/album_id/delete
    url(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),

    # /music/song/add
    url(r'song/add/$', views.SongCreate.as_view(), name='song-add'),

    url(r'song/$', views.SongView.as_view(), name='song'),

]
