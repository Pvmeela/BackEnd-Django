from django.shortcuts import render


from rest_framework import viewsets
from .models import (
    Usuario, Artista, Genero, Album, Cancion, 
    Playlist, PlaylistCancion, Favorito, Reproduccion, Seguidor, Historial
)

from .serializers import (
    UsuarioSerializer, ArtistaSerializer, GeneroSerializer, AlbumSerializer, CancionSerializer,
    PlaylistSerializer, PlaylistCancionSerializer, FavoritoSerializer, ReproduccionSerializer, SeguidorSerializer, HistorialSerializer
)
def bienvenida(request):
    return render(request, 'bienvenida.html')

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class ArtistaViewSet(viewsets.ModelViewSet):
    queryset = Artista.objects.all()
    serializer_class = ArtistaSerializer

class GeneroViewSet(viewsets.ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class CancionViewSet(viewsets.ModelViewSet):
    queryset = Cancion.objects.all()
    serializer_class = CancionSerializer

class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

class PlaylistCancionViewSet(viewsets.ModelViewSet):
    queryset = PlaylistCancion.objects.all()
    serializer_class = PlaylistCancionSerializer

class FavoritoViewSet(viewsets.ModelViewSet):
    queryset = Favorito.objects.all()
    serializer_class = FavoritoSerializer

class ReproduccionViewSet(viewsets.ModelViewSet):
    queryset = Reproduccion.objects.all()
    serializer_class = ReproduccionSerializer

class SeguidorViewSet(viewsets.ModelViewSet):
    queryset = Seguidor.objects.all()
    serializer_class = SeguidorSerializer

class HistorialViewSet(viewsets.ModelViewSet):
    queryset = Historial.objects.all()
    serializer_class = HistorialSerializer