from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from app.models import Student, Classroom
from registration.functions import checkUniqueEmail, checkAndFixUniqueUsername
from registration.forms import StudentRegistrationForm, DelegateRegistrationForm

def register(request):
	""" View for signing up, also includes a form for the students who have a link """

	if request.method == 'POST':
		form = StudentRegistrationForm(request.POST)

		if form.is_valid():
			hello_g = form.cleaned_data['code']
			messages.add_message(request, messages.SUCCESS, 'Ouiiiiiiiiii!')
	else:
		form = StudentRegistrationForm()

	return render(request, 'registration.html', locals())


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

































