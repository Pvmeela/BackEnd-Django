from django.contrib import admin

from .models import (
    Usuario, Artista, Genero, Album, Cancion, 
    Playlist, PlaylistCancion, Favorito, Reproduccion, Seguidor, Historial
)

# Registramos todos los modelos
admin.site.register(Usuario)
admin.site.register(Artista)
admin.site.register(Genero)
admin.site.register(Album)
admin.site.register(Cancion)
admin.site.register(Playlist)
admin.site.register(PlaylistCancion)
admin.site.register(Favorito)
admin.site.register(Reproduccion)
admin.site.register(Seguidor)
admin.site.register(Historial)
# Register your models here.
