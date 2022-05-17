from django.contrib import admin
from .models import Post, Bio, skills

# Register your models here.
admin.site.register(Post)
admin.site.register(Bio)
admin.site.register(skills)

