from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
	title = models.CharField(max_length=100)
	author = models.ForeignKey(User)
	pubDate = models.DateTimeField(auto_now=True,
								   verbose_name="Date de parution")
	content = models.CharField(max_length=10000)

	def __str__(self):
		return self.title