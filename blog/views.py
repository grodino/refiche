from django.shortcuts import render
from blog.models import Post

def home(request):
	""" Small blog to announce things about the website """

	posts = Post.objects.all().order_by('-pubDate')

	return render(request, 'blog/accueil.html', locals())