from django.http import Http404
from django.contrib.auth.models import User

def checkUniqueEmail(email):
	""" Check if the email address doesnt' exists (can't do it in the User model) """

	try:
		User.objects.get(email=email)
		raise Http404('Non à la guerre des clones! Il me semble que votre adresse email a déja été utilisée :/')
	except User.DoesNotExist:
		return


def checkAndFixUniqueUsername(username):
	""" Check if the user name is unique. If not add a number and increase it until it's unique """

	try:
		while User.objects.get(username=username):
			# If it's the second pass, don't add a number, just increase it
			# TODO: fix the infinit loop
			if username[-1].isnumeric():
				username.replace(username[-1], str(int(username[-1])+1))
			else:
				username += '1'
	except User.DoesNotExist:
		pass

	return username