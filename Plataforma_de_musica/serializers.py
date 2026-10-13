
from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from .models import (
    Usuario, Artista, Genero, Album, Cancion,
    Playlist, PlaylistCancion, Favorito,
    Reproduccion, Seguidor, Historial
)


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = [
            'id',
            'nombre_usuario',
            'correo',
            'contrasena',
            'tipo_usuario',
            'estado',
            'fecha_registro'
        ]
        extra_kwargs = {
            'contrasena': {
                'write_only': True,
                'required': True
            }
        }

    def create(self, validated_data):
        validated_data['contrasena'] = make_password(
            validated_data['contrasena']
        )
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if 'contrasena' in validated_data:
            validated_data['contrasena'] = make_password(
                validated_data['contrasena']
            )
        return super().update(instance, validated_data)


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
