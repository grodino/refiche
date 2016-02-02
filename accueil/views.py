# coding=UTF-8
from django.shortcuts import render

from app.functions import getStudent


def index(request):
	""" Start page of the website """

	if request.user.is_authenticated():
		student = getStudent(request.user)

	return render(request, 'accueil/login_accueil.html', locals())


def about(request):
	"""  About page for new students or new schools	"""

	return render(request, 'accueil/about.html', locals())