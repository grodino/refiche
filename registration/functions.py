from django.http import Http404
from django.contrib.auth.models import User, Group

from app.models import Student, Classroom
from notifications.models import NotificationSettings
from registration.models import StudentRegistrationCode

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
			if username[-1].isnumeric():
				username = username.replace(username[-1], str(int(username[-1])+1))
			else:
				username += '1'
	except User.DoesNotExist:
		pass

	return username


def checkStudentRegistrationCode(code):
	""" Check if the code submitted by the user exists
		If yes it returns the classroom object if not it returns None """

	try:
		verifiedCode = StudentRegistrationCode.objects.get(code=code)
	except StudentRegistrationCode.DoesNotExist:
		return None

	return verifiedCode.classroom


def createUserAndStudent(**kwargs):
	"""
	Create a user given the kwargs
	"""

	firstName = kwargs.get('firstName')
	lastName = kwargs.get('lastName')
	email = kwargs.get('email')
	password = kwargs.get('password')
	username = firstName[0].lower()+lastName.lower()
	avatar = kwargs.get('avatar')

	if len(username) > 30:
		username = username[:30]

	# Checks if the email is unique if not, throws Http404
	# And if it's ok, checks if the username is unique, if not change it until it is
	checkUniqueEmail(email)
	username = checkAndFixUniqueUsername(username)

	# Saving everything
	newUser = User.objects.create_user(username=username,
									   email=email,
									   password=password,
									   first_name=firstName,
									   last_name=lastName,
									   is_staff = kwargs.get('is_delegate'))

	if kwargs.get('is_delegate') is True:
		newUser.groups.add(Group.objects.get(name='delegates'))

	newUser.save()

	if kwargs.get('is_delegate') is True:
		newClassroom = Classroom(
			level=kwargs.get('level'),
			school=kwargs.get('school'),
			name=kwargs.get('classroomName'),
			shortName=kwargs.get('classroomShortName')
		)
		newClassroom.save()

		school = newClassroom.school
		classroom = newClassroom
	else:
		school = kwargs.get('code').classroom.school
		classroom = kwargs.get('code').classroom


	notificationSettings = NotificationSettings(
		groupedMailsEnabled=True,
		mailsEnabled=True
	)
	notificationSettings.save()

	newStudent = Student.objects.create(
		user=newUser,
		school=school,
		classroom=classroom,
		avatar=avatar,
		notificationsSettings=notificationSettings
	)
	newStudent.save()

	return newUser, newStudent


def createStudent():
	pass