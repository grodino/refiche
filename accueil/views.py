from django.shortcuts import render
import logging

def index(request):
	""" Start page of the website """

	return render(request, 'accueil/login_accueil.html', locals())
