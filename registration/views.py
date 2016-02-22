import json, logging, random, string
from django.conf import settings
from django.contrib import messages
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required, permission_required
from app.models import Student
from app.functions import getStudent
from facebook.functions import generateRandomKey
from facebook.models import CreateGroupToken, UserAccessToken
from registration.models import StudentRegistrationCode
from registration.functions import checkStudentRegistrationCode, createUserAndStudent, getRemoteImage
from registration.forms import DelegateRegistrationForm, RegistrationForm, StudentRegistrationForm, ChangeUserInfosForm


def register(request):
	""" View for signing up, also includes a form for the students who have a link """

	if request.method == 'POST':
		form = StudentRegistrationForm(request.POST)

		if form.is_valid():
			classroom = checkStudentRegistrationCode(form.cleaned_data['code'])

			if classroom is None: # If the code does not exist
				formUrl = None
				success = None
			else:
				formUrl = '/register/code/'+form.cleaned_data['code']
				success = 'true'

			return HttpResponse(json.dumps({'success': success,	'url': formUrl }), content_type='application/json')
	else:
		form = StudentRegistrationForm()

	return render(request, 'registration.html', locals())


def studentRegister(request, code):
	""" View made to let the students register themselves to their own classroom """
	try:
		code = StudentRegistrationCode.objects.get(code=code)
	except StudentRegistrationCode.DoesNotExist:
		raise PermissionDenied('Votre code n\'est pas valide :\ ')

	if request.method == 'POST':
		form = RegistrationForm(data=request.POST, files=request.FILES)

		if form.is_valid():
			newUser, newStudent = createUserAndStudent(
				firstName=form.cleaned_data['firstName'],
				lastName=form.cleaned_data['lastName'],
				email=form.cleaned_data['email'],
				password=form.cleaned_data['password2'],
				avatar=form.cleaned_data['avatar'],
				is_delegate=False,
				code=code
			)

			newUser.email_user('Votre inscription sur REFICHE', """Vous êtes maintenant inscrit(e), voici vos identifiants, conservez les!
																   Nom d\'utilisateur: {}
																   Mot de passe: Vous seul le connaissez""".format(newUser.username), from_email='contact@refiche.fr')

			classroomDelegates = Student.objects.filter(classroom=newStudent.classroom).filter(user__is_staff=True)

			# TODO: Use the notification system
			send_mail('REFICHE ' + newStudent.classroom.name + 'administration',
					  'Une personne s\'est inscrite à votre classe : ' + newUser.first_name + newUser.last_name.upper(),
					  'contact@refiche.fr',
					  [delegate.user.email for delegate in classroomDelegates])


			is_delegate = False

			return redirect('registration:registerSuccess', profileType='student')
	else: 
		form = RegistrationForm()

	return render(request, 'registration/student_register.html', locals())


def delegateRegister(request):
	""" View for registration by the delegate of the classroom """

	if request.method == 'POST':
		form = DelegateRegistrationForm(data=request.POST, files=request.FILES)

		if form.is_valid():
			# Fetching user data and creating a username
			newUser, newStudent = createUserAndStudent(
				firstName=form.cleaned_data['firstName'],
				lastName=form.cleaned_data['lastName'],
				email=form.cleaned_data['email'],
				password=form.cleaned_data['password2'],
				avatar=form.cleaned_data['avatar'],
				is_delegate=True,
				level=form.cleaned_data['classroomLevel'],
				school=form.cleaned_data['school'],
				classroomName=form.cleaned_data['classroomName'],
				classroomShortName=form.cleaned_data['classroomShortName']
			)

			is_delegate = True

			token = CreateGroupToken()
			token.delegate = newUser
			token.save()

			# TODO: Use the notification system
			newUser.email_user('Votre inscription sur REFICHE', """Vous êtes maintenant inscrit(e), voici vos identifiants, conservez les!
																   Nom d\'utilisateur: {}
																   Mot de passe: Vous seul le connaissez""".format(newUser.username), from_email='contact@refiche.fr')

			return redirect('registration:registerSuccess', profileType='delegate', token=token.value)
	else:
		form = DelegateRegistrationForm()

	return render(request, 'registration/delegate_register.html', locals())


def registerUserFacebook(request, profileType):
	"""
	Register a user who wants to sign in with facebook
	"""
	logger = logging.getLogger('registration')

	facebook_code = request.GET['code']
	access_token = UserAccessToken()

	# TODO : handle facebook registration flow for delegates
	if profileType == 'delegate':
		redirect_uri = settings.FACEBOOK_SETTINGS['OAUTH_REDIRECT_URI'] + 'delegate/'
		logger.warn('Someone tried to register with facebook as a delegate and failed')

		raise Http404('Désolé, en tant que délégué vous ne pouvez pas vous inscrive avec facebook pour l\'instant :(')
	else:
		try:
			code = StudentRegistrationCode.objects.get(code=profileType)
		except StudentRegistrationCode.DoesNotExist:
			logger.info('Someone tried to register as a student with the wrong registration code')

			raise PermissionDenied('Votre code n\'est pas valide :\ ')

		redirect_uri = settings.FACEBOOK_SETTINGS['OAUTH_REDIRECT_URI'] + profileType + '/'

	access_token.fetchAccessToken(facebook_code, redirect_uri)
	user_info = access_token.fetchUserInfo()

	avatar = getRemoteImage(user_info['avatar_url'])
	password = generateRandomKey(10)

	newUser, newStudent = createUserAndStudent(
		firstName=user_info['first_name'],
		lastName=user_info['last_name'],
		email=user_info['email'],
		password=password,
		avatar=avatar,
		is_delegate=False,
		code=code,
		facebook_id=user_info['facebook_id']
	)

	newUser.email_user('Votre inscription sur REFICHE', """Vous êtes maintenant inscrit(e) sur Refiche !
															Pour vous connecter sur refiche.fr avec votre compte facebook, cliquez sur \"se connecter avec facebook\"""", from_email='contact@refiche.fr')

	classroomDelegates = Student.objects.filter(classroom=newStudent.classroom).filter(user__is_staff=True)

	# TODO: Use the notification system
	send_mail('REFICHE ' + newStudent.classroom.name + 'administration',
			  'Une personne s\'est inscrite à votre classe : ' + newUser.first_name + newUser.last_name.upper(),
			  'contact@refiche.fr',
			  [delegate.user.email for delegate in classroomDelegates])

	logger.info('User {user.first_name} {user.last_name} as registered to REFICHE !'.format(user=newUser))
	messages.add_message(request, messages.SUCCESS, 'Vous êtes maintenant inscrit sur Refiche, bienvenue ;)')

	user = authenticate(
		fb_id=user_info['facebook_id']
	)

	if user is not None:
		login(request, user)
		return redirect('app:home')

	return redirect('registration:registerSuccess', profileType='student')


def registerSuccess(request, profileType, token):
	"""
	View where the user is redirected after a successful registration
	"""

	if profileType == 'delegate':
		is_delegate = True
	else:
		is_delegate = None

	return render(request, 'registration/register_success.html', locals())


@login_required
def changeUserInfos(request):
	""" Ajax view where the user can modify his information """
	student = getStudent(request.user)

	if request.method == 'POST':
		form = ChangeUserInfosForm(request.POST)

		if form.is_valid():
			firstName = form.cleaned_data['firstName']
			lastName = form.cleaned_data['lastName']
			password = form.cleaned_data['password2']
			avatar = form.cleaned_data['avatar']

			student.user.last_name = lastName
			student.user.first_name = firstName
			student.user.set_password(password)
			student.user.save()

			student.avatar = avatar
			student.save()

			JSONResponse = json.dumps({'success': 'true'})
		else:
			JSONResponse = json.dumps(form.errors)

		return HttpResponse(JSONResponse, content_type='application/json')
	else:
		form = ChangeUserInfosForm(
			initial={ 'firstName': student.user.first_name,
					  'lastName': student.user.last_name,
					  'avatar': student.avatar }
		)

	return render(request, 'registration/change_user_infos.html', locals())






























