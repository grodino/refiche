from django.db import models

class Article(models.Model):
	titre = models.CharField(max_length=100)
	auteur = models.CharField(max_length=42)
	contenu = models.DateTimeField(auto_now_add=True, auto_now=False,
								   verbose_name="Date de parution")

	def __str__(self):
		""" Permet de reconnaitre l'objet dans l'administration """

		return self.titre

class Categorie(models.Model):
	nom = models.CharField(max_length=30)

	def __str__(self):
		return self.titre