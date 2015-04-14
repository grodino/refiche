from django.shortcuts import render
import logging

def home(request):
	""" Test d'affiche de templates cours OpenClassrooms """

	logger = logging.getLogger('django')
	logger.info('------------- A non-logged visitor is checking the Blog ! -------------')

	return render(request, 'blog/accueil.html', locals())