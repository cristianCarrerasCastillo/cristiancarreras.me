from django.db import models
from ckeditor.fields import RichTextField

#ToDo:
# - Create a repo for images
# - Delete hrs in inicio and final when creating a new post, only have a day

class Post(models.Model):
    empresa = models.CharField(max_length=200, verbose_name='Empresa')
    cargo = models.CharField(max_length=100, verbose_name='Cargo')
    body = RichTextField(verbose_name='Descripción del puesto')
    inicio = models.DateField(verbose_name='Fecha de inicio',blank=True, null=True)
    final = models.DateField(verbose_name='Fecha de finalización', blank=True, null=True)
    logo = models.ImageField(verbose_name='Logo de la empresa', upload_to='logos', blank=True, null=True)
    linkEmpresa = models.URLField(verbose_name='Link de la empresa', blank=True, null=True)

    class Meta:
        verbose_name = 'Experiencia Laboral'
        verbose_name_plural = 'Experiencia Laboral'
    def __str__(self):
        return self.empresa

class Bio(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    apellido = models.CharField(max_length=100, verbose_name='Apellido')
    nacionalidad = models.CharField(max_length=100, verbose_name='Ubicación', blank=True, null=True)
    telefono = models.CharField(max_length=100, verbose_name='Teléfono', blank=True, null=True)
    correo = models.EmailField(verbose_name='Correo electrónico', blank=True, null=True)
    linkedin = models.URLField(verbose_name='Linkedin', blank=True, null=True)
    github = models.URLField(verbose_name='Github', blank=True, null=True)
    bio = RichTextField(verbose_name='Biografía')

    class Meta:
        verbose_name = 'Biografía'
        verbose_name_plural = 'Biografía'
    def __str__(self):
        return (self.nombre + ' ' + self.apellido)

class skills(models.Model):
    skill = models.CharField(max_length=50, verbose_name='Habilidad')
    porcentaje = models.IntegerField(verbose_name='Nivel de conocimiento (Hasta 6)')

    class Meta:
        verbose_name_plural = 'Habilidades'

    def __str__(self):
        return self.skill
