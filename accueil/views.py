from django.shortcuts import render
from django.conf import settings
import logging, requests

def index(request):
	""" Start page of the website """

	return render(request, 'accueil/login_accueil.html', locals())
