from rest_framework import serializers
from .models import (
    Usuario, Artista, Genero, Album, Cancion, 
    Playlist, PlaylistCancion, Favorito, Reproduccion, Seguidor, Historial
)

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class ArtistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artista
        fields = '__all__'

class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'

class CancionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cancion
        fields = '__all__'

class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = '__all__'

class PlaylistCancionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaylistCancion
        fields = '__all__'

class FavoritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorito
        fields = '__all__'

class ReproduccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reproduccion
        fields = '__all__'

class SeguidorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seguidor
        fields = '__all__'

class HistorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historial
        fields = '__all__'