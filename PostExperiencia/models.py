from django.db import models

#ToDo:
# - Create a repo for images
# - Delete hrs in inicio and final when creating a new post, only have a day

class Post(models.Model):
    empresa = models.CharField(max_length=200, verbose_name='Empresa')
    cargo = models.CharField(max_length=100, verbose_name='Cargo')
    body = models.TextField(verbose_name='Descripción del puesto')
    inicio = models.DateTimeField(verbose_name='Fecha de inicio',blank=True, null=True)
    final = models.DateTimeField(verbose_name='Fecha de finalización', blank=True, null=True)
    logo = models.ImageField(verbose_name='Logo de la empresa', upload_to='logos', blank=True, null=True)
    def __str__(self):
        return self.empresa
