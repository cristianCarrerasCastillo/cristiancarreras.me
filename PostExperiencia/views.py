from django.shortcuts import render
from PostExperiencia.models import Post
from .models import Post, Bio, skills

# Create your views here.
def cv(request):
    post = Post.objects.all()
    bio = Bio.objects.all()
    #skills = skills.objects.all()
    return render(request, 'index.html', {'post': post, 'bio': bio})

