from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UsuarioViewSet, ArtistaViewSet, GeneroViewSet, AlbumViewSet, CancionViewSet,
    PlaylistViewSet, PlaylistCancionViewSet, FavoritoViewSet, ReproduccionViewSet, SeguidorViewSet, HistorialViewSet
)

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'artistas', ArtistaViewSet)
router.register(r'generos', GeneroViewSet)
router.register(r'albums', AlbumViewSet)
router.register(r'canciones', CancionViewSet)
router.register(r'playlists', PlaylistViewSet)
router.register(r'playlist-canciones', PlaylistCancionViewSet)
router.register(r'favoritos', FavoritoViewSet)
router.register(r'reproducciones', ReproduccionViewSet)
router.register(r'seguidores', SeguidorViewSet)
router.register(r'historial', HistorialViewSet)

urlpatterns = [
    path('', include(router.urls)),
]