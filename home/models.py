from django.db import models
from django.contrib.auth.models import User


class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    imagenUrl = models.URLField(blank=True, null=True)
    nivel = models.IntegerField(default=1)
    ranking = models.IntegerField(default=0)

    def __str__(self):
        return self.nickname


class EspecieMarina(models.Model):
    nombre = models.CharField(max_length=120, default="Desconocido")
    nombreCientifico = models.CharField(max_length=150, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    imagenUrl = models.URLField(blank=True, null=True)


    def __str__(self):
        return self.nombre


class EspecieEnPeligro(models.Model):
    especie = models.ForeignKey(EspecieMarina, on_delete=models.CASCADE)
    nivelRiesgo = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.especie.nombre} - {self.nivelRiesgo}"


class HabitatMarino(models.Model):
    nombre = models.CharField(max_length=100)
    region = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre


class EspecieHabitat(models.Model):
    especie = models.ForeignKey(EspecieMarina, on_delete=models.CASCADE, null=True, blank=True)
    habitat = models.ForeignKey(HabitatMarino, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        unique_together = ('especie', 'habitat')


class AmenazaMarina(models.Model):
    nombre = models.CharField(max_length=120)
    tipo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre


class Contaminante(models.Model):
    nombre = models.CharField(max_length=120)
    categoria = models.CharField(max_length=100)
    peligrosidad = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class AmenazaContaminante(models.Model):
    amenaza = models.ForeignKey(AmenazaMarina, on_delete=models.CASCADE)
    contaminante = models.ForeignKey(Contaminante, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('amenaza', 'contaminante')


class RecursoEducativo(models.Model):
    titulo = models.CharField(max_length=150)
    tipo = models.CharField(max_length=80)
    descripcion = models.TextField(blank=True, null=True)
    url = models.URLField()

    def __str__(self):
        return self.titulo


class CentroInvestigacion(models.Model):
    nombre = models.CharField(max_length=150)
    direccion = models.CharField(max_length=200)
    pais = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre


class OrganizacionProteccion(models.Model):
    nombre = models.CharField(max_length=150)
    mision = models.TextField()
    region = models.CharField(max_length=150)

    def __str__(self):
        return self.nombre


class ProyectoOrganizacion(models.Model):
    organizacion = models.CharField(max_length=150, null=True, blank=True)
    nombre = models.CharField(max_length=150, blank=True, null=True)
    descripcion = models.TextField(null=True, blank=True)
    fechaInicio = models.DateField(blank=True, null=True)
    fechaFin = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.nombre


class AreaProtegida(models.Model):
    nombre = models.CharField(max_length=150)
    region = models.CharField(max_length=150, default="Desconocido")
    descripcion = models.TextField(blank=True, null=True)
    tamañoKm2 = models.DecimalField(
    max_digits=10,
    decimal_places=2,
    default=0.00
)

    def __str__(self):
        return self.nombre


class Nivel(models.Model):
    nombre = models.CharField(max_length=100)
    dificultad = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class PuntajeJuego(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    puntaje = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.puntaje}"


class Logro(models.Model):
    nombre = models.CharField(max_length=120, null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.nombre


# FALTABA ESTE MODELO → ahora agregado
class UsuarioLogro(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    logro = models.ForeignKey(Logro, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario', 'logro')

    def __str__(self):
        return f"{self.usuario.username} - {self.logro.nombre}"


class EventoMarino(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(null=True, blank=True)
    fecha = models.DateField(null=True, blank=True)  # ← añadir
    region = models.CharField(max_length=150, null=True, blank=True)  # ← agregar

    def __str__(self):
        return self.nombre



class Amigos(models.Model):
    usuario1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuario1")
    usuario2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuario2")
    estado = models.CharField(max_length=20, default='pendiente')
    fechaSolicitud = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario1', 'usuario2')


class Chat(models.Model):
    emisor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="mensajes_enviados")
    receptor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="mensajes_recibidos")
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.emisor.username} → {self.receptor.username}"
    
    