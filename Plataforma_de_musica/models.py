from django.db import models



class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=50)
    correo = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=100)
    tipo_usuario = models.CharField(max_length=20, default="Oyente")
    estado = models.BooleanField(default=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre_usuario


class Artista(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nombre_artistico = models.CharField(max_length=100)
    pais = models.CharField(max_length=50)
    biografia = models.TextField(null=True, blank=True)
    verificado = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre_artistico


class Genero(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nombre


class Album(models.Model):
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    fecha_lanzamiento = models.DateField()
    portada = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.titulo


class Cancion(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    duracion = models.IntegerField()
    numero_pista = models.IntegerField()
    fecha_lanzamiento = models.DateField()
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo


class Playlist(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    publica = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class PlaylistCancion(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    cancion = models.ForeignKey(Cancion, on_delete=models.CASCADE)
    posicion = models.IntegerField()
    fecha_agregada = models.DateTimeField(auto_now_add=True)


class Favorito(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    cancion = models.ForeignKey(Cancion, on_delete=models.CASCADE)
    fecha_agregado = models.DateTimeField(auto_now_add=True)


class Reproduccion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    cancion = models.ForeignKey(Cancion, on_delete=models.CASCADE)
    fecha_reproduccion = models.DateTimeField(auto_now_add=True)
    segundos_escuchados = models.IntegerField()
    dispositivo = models.CharField(max_length=50)


class Seguidor(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    fecha_seguimiento = models.DateTimeField(auto_now_add=True)


class Historial(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    accion = models.CharField(max_length=100)
    entidad = models.CharField(max_length=50)
    id_entidad = models.IntegerField()
    descripcion = models.TextField(null=True, blank=True)
    fecha_accion = models.DateTimeField(auto_now_add=True)
# Create your models here.
