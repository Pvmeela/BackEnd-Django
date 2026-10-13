
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.shortcuts import render

from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import redirect


from rest_framework import viewsets
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
    IsAdminUser
)

from .models import (
    Usuario, Artista, Genero, Album, Cancion,
    Playlist, PlaylistCancion, Favorito,
    Reproduccion, Seguidor, Historial
)

from .serializers import (
    UsuarioSerializer, ArtistaSerializer, GeneroSerializer,
    AlbumSerializer, CancionSerializer, PlaylistSerializer,
    PlaylistCancionSerializer, FavoritoSerializer,
    ReproduccionSerializer, SeguidorSerializer,
    HistorialSerializer
)


# Pagina de bienvenida
def bienvenida(request):
    return render(request, 'bienvenida.html')


# Vista basada en funcion (FBV)
@login_required
def vista_protegida_funcional(request):
    return render(request, 'dashboard.html')


# Vista basada en clase (CBV)
class VistaProtegidaClase(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'


# API de usuarios: solo administradores
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAdminUser]


# API de artistas
class ArtistaViewSet(viewsets.ModelViewSet):
    queryset = Artista.objects.all()
    serializer_class = ArtistaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# API de generos
class GeneroViewSet(viewsets.ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# API de albumes
class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# API de canciones
class CancionViewSet(viewsets.ModelViewSet):
    queryset = Cancion.objects.all()
    serializer_class = CancionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# API de playlists
class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# API de canciones en playlists
class PlaylistCancionViewSet(viewsets.ModelViewSet):
    queryset = PlaylistCancion.objects.all()
    serializer_class = PlaylistCancionSerializer
    permission_classes = [IsAuthenticated]


# API de favoritos
class FavoritoViewSet(viewsets.ModelViewSet):
    queryset = Favorito.objects.all()
    serializer_class = FavoritoSerializer
    permission_classes = [IsAuthenticated]


# API de reproducciones
class ReproduccionViewSet(viewsets.ModelViewSet):
    queryset = Reproduccion.objects.all()
    serializer_class = ReproduccionSerializer
    permission_classes = [IsAuthenticated]


# API de seguidores
class SeguidorViewSet(viewsets.ModelViewSet):
    queryset = Seguidor.objects.all()
    serializer_class = SeguidorSerializer
    permission_classes = [IsAuthenticated]


# API de historial
class HistorialViewSet(viewsets.ModelViewSet):
    queryset = Historial.objects.all()
    serializer_class = HistorialSerializer
    permission_classes = [IsAuthenticated]


def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registro exitoso. ¡Bienvenido!")
            return redirect('bienvenida')
        else:
            messages.error(request, "Revisa los datos del formulario.")
    else:
        form = UserCreationForm()

    return render(request, 'registration/registro.html', {'form': form})