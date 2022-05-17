from django.shortcuts import render
from PostExperiencia.models import Post
from .models import Post

# Create your views here.
def cv(request):
    post = Post.objects.all()
    return render(request, 'index.html', {'post': post})

