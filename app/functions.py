import logging
from django.http import Http404
from app.models import Student

def getStudent(request):
	""" /!\ Not a view, it fetches the user and verifiy if there
		is a profile account logged to it. RETURNS THE STUDENT """

	user = request.user
	
	try:
		student = Student.objects.get(user=user)
	except Student.DoesNotExist:
		logger = logging.getLogger('users')
		logger.error(user.username+'\'s account is not linked to a profile account! id = '+str(user.id))
		raise Http404("Your user account is not linked to a profile account !")

	return student