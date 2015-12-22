# coding=UTF-8
import logging
from os import remove, popen
from os.path import splitext, join
from datetime import timedelta
from django.conf import settings
from django.http import Http404
from django.utils import timezone


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


def getSheetInstance(pk):
	""" Get a specific sheet without any checks,
	 	basically just to see if it exists """
	from app.models import Sheet

	# Get the file
	try:
		sheet = Sheet.objects.get(pk=pk)
	except Sheet.DoesNotExist:
		raise Http404("Sorry this file does not exist :(")

	return sheet


def getLastSheetsForLesson(instance, numberOfSheets):
	""" Get the [numberOfSheets] most recents sheets in the lesson
		instance and return them as an array, returns an empty array 
		if there are no sheets or if they are too old (>2 weeks) """
	from app.models import Sheet

	timeLimit = timezone.now() - timedelta(weeks=2)
	sheets = Sheet.objects.filter(lesson=instance, uploadDate__gte=timeLimit).order_by('-uploadDate')[:numberOfSheets]

	return sheets


def getLastLinksForLesson(instance, numberOfLinks):
	from app.models import Link

	timeLimit = timezone.now() - timedelta(weeks=2)
	links = Link.objects.filter(lesson=instance, uploadDate__gte=timeLimit).order_by('-uploadDate')[:numberOfLinks]

	return links


def getLastSheetsForClassroom(instance, numberOfSheets):
	""" Get the last sheets published in a classroom in the numberOfSheets range """
	from app.models import Sheet

	sheets = Sheet.objects.filter(lesson__in=instance.lessons.all()).order_by('-uploadDate')[:numberOfSheets]

	return sheets


def getLastLinksForClassroom(instance, numberOfLinks):
	""" Get the last sheets published in a classroom in the numberOfSheets range """
	from app.models import Link

	links = Link.objects.filter(lesson__in=instance.lessons.all()).order_by('-uploadDate')[:numberOfLinks]

	return links


def getFilesForSheet(instance):
	"""
	Get all the UploadedFiles related to a Sheet object
	"""
	from app.models import UploadedFile

	fileSet = UploadedFile.objects.filter(relatedSheet=instance)

	return fileSet


def renameFile(instance, name):
	""" It's a function made to modify the name
		of the file like this it won't be executed """

	extension = splitext(name)[1].replace('.', 'point-')
	fileName = splitext(name)[0]

	return "sheets/{}-{}".format(fileName, extension)


def deleteSheet(sender, instance, **kwargs):
	""" Function made to deduct 1 from the user's numberOfSheetsUploaded """

	# Deduct 1 from the user's numberOfSheetsUploaded
	student = instance.uploadedBy
	student.numberOfItemsUploaded = student.numberOfItemsUploaded - 1
	student.save()

	if instance.thumbnail.name is not None:
		remove(join(settings.MEDIA_ROOT, instance.thumbnail.name))


def deleteFile(sender, instance, **kwargs):
	"""
	Function made to remove 'physically' the file file related to the
	UploadedFile models
	"""

	remove(join(settings.MEDIA_ROOT, instance.file.name))


def deleteLink(sender, instance, **kwargs):
	""" Function made to delete the link's thumbnail form the os """

	student = instance.uploadedBy
	student.numberOfItemsUploaded = student.numberOfItemsUploaded - 1
	student.save()

	if instance.hasThumbnail():
		remove(join(settings.MEDIA_ROOT, instance.thumbnail))


def addSheet(sender, instance, **kwargs):
	""" Function made to add 1 to the user's numberOfSheetsUploaded """
	from notifications.models import NotificationManager

	student = instance.uploadedBy
	student.numberOfItemsUploaded = student.numberOfItemsUploaded + 1
	student.save()

	classroom = instance.uploadedBy.classroom

	nm = NotificationManager()
	nm.notifyClassroom(
		classroom=classroom,
		sender=sender,
		instance=instance
	)


def addLink(sender, instance, **kwargs):
	""" Function made to add 1 to the user's numberOfItemsUploaded """
	from notifications.models import NotificationManager

	student = instance.uploadedBy
	student.numberOfItemsUploaded = student.numberOfItemsUploaded + 1
	student.save()

	classroom = instance.uploadedBy.classroom

	nm = NotificationManager()
	nm.notifyClassroom(
		classroom=classroom,
		sender=sender,
		instance=instance
	)


def deleteUser(sender, instance, **kwargs):
	""" Function to delete the Student object associated to the user when you delete it """
	from app.models import Student

	student = getStudent(instance)
	student.delete()
