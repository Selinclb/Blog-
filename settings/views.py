from settings.models import Settings
from django.shortcuts import render
from blog.models import Post

def home(request):
    posts = Post.objects.all()
    site_config = Settings.objects.first()
    return render(request, 'blog/home.html', {'posts': posts, 'site_config': site_config})

