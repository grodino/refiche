# coding=UTF-8
from django.shortcuts import render

def index(request):
	""" Start page of the website """

	return render(request, 'accueil/login_accueil.html', locals())


def about(request):
	"""  About page for new students or new schools	"""

	return render(request, 'accueil/about.html', locals())