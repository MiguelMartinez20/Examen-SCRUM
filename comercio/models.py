from django.db import models
from django.utils import timezone

# Create your models here.

class Productor(models.Model):

    ACTIVA = 'Activa'
    DESHABILITADA = 'Deshabilitada'

    STATE_CHOICES = (
        (ACTIVA, 'Activa'),
        (DESHABILITADA, 'Deshabilitada'),
    )

    rut = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    latitud = models.CharField(max_length=200)
    longitud = models.CharField(max_length=200)
    pyme = models.CharField(max_length=200,blank=True)
    email = models.CharField(max_length=200)
    cuenta = models.CharField(max_length=10, choices=STATE_CHOICES, default=ACTIVA)

    def publish(self):
        self.save()

    def str(self):
        return self.rut

class Producto(models.Model):

    nombre = models.CharField(max_length=200)
    detalle = models.CharField(max_length=200)
    precio = models.CharField(max_length=200)
    productor = models.ForeignKey(Productor, on_delete=models.CASCADE, blank=True, null=True)

    def publish(self):
        self.save()

    def str(self):
        return self.nombre

class Post(models.Model):

    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def str(self):
        return self.title

class Solicitud(models.Model):

    rut = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    pyme = models.CharField(max_length=200,blank=True)
    email = models.CharField(max_length=200)

    def publish(self):
        self.save()

    def str(self):
        return self.rut

class Pedido(models.Model):

    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    detalle = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    date_time = models.DateTimeField(default=timezone.now)


    def publish(self):
        self.date_time = timezone.now()
        self.save()

    def str(self):
        return self.nombre







