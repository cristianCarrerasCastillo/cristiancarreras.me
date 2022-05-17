from django.db import models

#ToDo:
# - Create a repo for images
# - Delete hrs in inicio and final when creating a new post, only have a day

class Post(models.Model):
    empresa = models.CharField(max_length=200)
    body = models.TextField()
    inicio = models.DateTimeField()
    final = models.DateTimeField()
    logo = models.ImageField()
    def __str__(self):
        return self.empresa
