# coding=UTF-8
import logging
from os import remove, popen
from os.path import splitext, join
from django.conf import settings
from django.http import Http404

def getStudent(instance):
	""" /!\ Not a view, it fetches the user and verifiy if there
		is a profile account logged to it. RETURNS THE STUDENT """
	from app.models import Student

	user = instance
	
	try:
		student = Student.objects.get(user=user)
	except Student.DoesNotExist:
		logger = logging.getLogger('users')
		logger.error(user.username+'\'s account is not linked to a profile account! id = '+str(user.id))
		raise Http404("Your user account is not linked to a profile account !")

	return student


def renameFile(instance, name):
	""" It's a function made to modify the name
		of the file like this it won't be executed """

	extension = splitext(name)[1].replace('.', 'point-')
	fileName = splitext(name)[0]

	return "sheets/{}-{}".format(fileName, extension)


def deleteFile(sender, instance, **kwargs):
	""" Function made to delete a file and deduct 1 from the user's numberOfSheetsUploaded"""

	# Deduct 1 from the user's numberOfSheetsUploaded
	user = instance.uploadedBy
	user.numberOfSheetsUploaded = user.numberOfSheetsUploaded - 1
	user.save()

	remove(join(settings.MEDIA_ROOT, instance.sheetFile.name))


def addFile(sender, instance, **kwargs):
	""" Function made to add 1 to the user's numberOfSheetsUploaded """

	user = instance.uploadedBy
	user.numberOfSheetsUploaded = user.numberOfSheetsUploaded + 1
	user.save()

def deleteUser(sender, instance, **kwargs):
	""" Function to delete the Student object associated to the user when you delete it """
	from app.models import Student

	student = getStudent(instance)
	student.delete()
