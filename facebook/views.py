import json
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.http import Http404, HttpResponse
from django.shortcuts import redirect

from app.functions import getStudent
from facebook.backend import FacebookBackend
from facebook.models import CreateGroupToken, ClassGroup, UserAccessToken


def facebook_login(request):
	"""
	Login the User with the facebook authentication backend
	"""

	if request.user.is_authenticated():
		return redirect('app:home')

	# Get the facebook access token from the code returned
	facebook_code = request.GET['code']
	access_token = UserAccessToken()
	redirect_uri = settings.FACEBOOK_SETTINGS['LOGIN_REDIRECT_URI']

	# Get the user information (especially the user_id)
	# Like this the user_id is not passing via the client
	access_token.fetchAccessToken(facebook_code, redirect_uri)
	user_info = access_token.fetchUserInfo()

	user = authenticate(
		fb_id=user_info['facebook_id']
	)

	if user is not None:
		login(request, user)
		return redirect('app:home')
	else:
		raise Http404('Vous ne vous êtes pas inscrit ou vous devez renseigner votre compte facebook')


def createClassroomGroup(request, tokenValue, facebookUserId):
	""" Creates a classroom group for the user that claimed it
	 	/!\ The user is fetched by the token, that's why there is not decorator"""

	# Check if the token exists
	try:
		token = CreateGroupToken.objects.get(value=tokenValue)
	except CreateGroupToken.DoesNotExist:
		raise Http404('Votre token n\'existe pas !')

	student = getStudent(token.delegate)
	classroom = student.classroom

	fbGroup = ClassGroup()
	fbGroup.groupId = fbGroup.createClassGroup(student, facebookUserId)
	fbGroup.name = classroom.name
	fbGroup.save()

	token.delete()

	return HttpResponse(
		json.dumps({'success': True,
					'id': fbGroup.groupId}),
		content_type='application/json'
	)