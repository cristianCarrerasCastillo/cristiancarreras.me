from django.db import models


class Post(models.Model):
    empresa = models.CharField(max_length=200)
    body = models.TextField()
    inicio = models.DateTimeField()
    final = models.DateTimeField()
    def __str__(self):
        return self.empresa
