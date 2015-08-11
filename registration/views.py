import json, logging, random, string
from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required, permission_required
from app.models import Student, Classroom
from app.functions import getStudent
from registration.functions import checkUniqueEmail, checkAndFixUniqueUsername, checkStudentRegistrationCode
from registration.forms import StudentRegistrationForm, DelegateRegistrationForm, StudentCodeRegistrationForm


def register(request):
	""" View for signing up, also includes a form for the students who have a link """

	if request.method == 'POST':
		form = StudentCodeRegistrationForm(request.POST)

		if form.is_valid():
			classroom = checkStudentRegistrationCode(form.cleaned_data['code'])

			if classroom is None: # If the code does not exist
				# TODO: return an error message probably in JSON
				formUrl = None
				success = None
			else:
				formUrl = 'url where the user is going to be redirected'
				success = 'true'

			return HttpResponse(json.dumps({'success': success,	'url': formUrl }), content_type='application/json')
	else:
		form = StudentCodeRegistrationForm()

	return render(request, 'registration.html', locals())


@login_required
@permission_required('registration.add_studentregistrationcode')
def getCode(request):
	""" View made to get a code valid for limited number of student to be able to sign up """

	student = getStudent(request.user)

	if request.method == 'POST':
		form = StudentRegistrationForm(request.POST)

		if form.is_valid():
			code = form.save(commit=False)

			# Create a random string of 20 chars for the code
			code.code = ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(20))
			code.classroom = student.classroom
			code.numberOfStudentsLeft = code.numberOfStudents
			code.save()

			JSONResponse = json.dumps({'sucess': 'true', 'code': code.code})
		else:
			JSONResponse = json.dumps(form.errors)
	else:
		raise Http404('Hey :/ I wasn\'t expecting you here !')

	return HttpResponse(JSONResponse, content_type='application/json')


def studentRegister(request):
	""" View made to let the students register themselves to their own classroom """

	return render(request, 'student_register', locals())


def delegateRegister(request):
	""" View for registration by the delegate of the classroom """

	if request.method == 'POST':
		form = DelegateRegistrationForm(request.POST)

		if form.is_valid():
			# Fetching user data and creating a username
			firstName = form.cleaned_data['firstName']
			lastName = form.cleaned_data['lastName']
			email = form.cleaned_data['email']
			password = form.cleaned_data['password2']
			username = firstName[0].lower()+lastName.lower()

			if len(username) > 30:
				username = username[:31]

			# Fetching classroom's information
			school = form.cleaned_data['school']
			classroomName = form.cleaned_data['classroomName']
			classroomShortName = form.cleaned_data['classroomShortName']
			classroomLevel = form.cleaned_data['classroomLevel']

			# Checks if the email is unique if not, throws Http404
			# And if it's ok, checks if the username is unique, if not change it until it is
			checkUniqueEmail(email)
			username = checkAndFixUniqueUsername(username)

			# Saving everything
			newUser = User.objects.create_user(username=username,
											   email=email,
											   password=password,
											   first_name=firstName,
											   last_name=lastName,)
			newUser.is_staff = True
			newUser.groups.add(Group.objects.get(name='delegates'))
			newUser.save()

			newClassroom = Classroom(level=classroomLevel,
									 school=school,
									 name=classroomName,
									 shortName=classroomShortName)
			newClassroom.save()

			newDelegate = Student.objects.create(user=newUser,
												 school=school,
												 classroom=newClassroom)
			newDelegate.save()

			newUser.email_user('Votre inscription sur REFICHE', """Vous êtes maintenant inscrit(e), voici vos identifiants, conservez les!
																   Nom d\'utilisateur: {}
																   Mot de passe: {}""".format(username, password))

			return render(request, 'registration/register_success.html', locals())
	else:
		form = DelegateRegistrationForm()

	return render(request, 'registration/delegate_register.html', locals())

































