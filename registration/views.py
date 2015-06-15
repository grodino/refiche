from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User
from app.models import Student, Classroom
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


			# Saving everything
			newUser = User.objects.create_user(username=username,
											   email=email,
											   password=password,
											   first_name=firstName,
											   last_name=lastName)
			newClassroom = Classroom(level=classroomLevel,
									 school=school,
									 name=classroomName,
									 shortName=classroomShortName)
			newClassroom.save()

			newDelegate = Student.objects.create(user=newUser,
												 school=school,
												 classroom=newClassroom)
			newDelegate.save()

			messages.add_message(request, messages.SUCCESS, 'Vous êtes bien inscrit!')
	else:
		form = DelegateRegistrationForm()

	return render(request, 'registration/delegate_register.html', locals())