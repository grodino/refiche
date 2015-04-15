# coding=UTF-8
from os.path import splitext
from django.db import models
from django.contrib.auth.models import User
from django.core.files import File

def renameFile(instance, name):
	""" NOT A MODEL, it's a function made to modify the name 
		of the file like this it won't be executed """
	extension = splitext(name)[1].replace('.', 'point-')
	fileName = splitext(name)[0]
	return "sheets/{}-{}".format(extension, fileName)


class Lesson(models.Model):
	""" The lesson/class model, they can only be created by a delegate """

	name = models.CharField(max_length=30) # The official name of the class
	teacher = models.ForeignKey('Teacher') # The link to the teacher (one teacher for one class)

	def __str__(self):	
		return "{0} ({1})".format(self.name, self.teacher)


class Level(models.Model):
	""" Level/ degree model, they can only be created by myself now
		It might change in the future"""

	name = models.CharField(max_length=30) # The official name of the level/degree

	def __str__(self):
		return self.name


class School(models.Model):
	""" School model, it can refer to many levels (primaire, collège ...) """
	
	name = models.CharField(max_length=255) # The full name of the school chosen by the user
	levels = models.ManyToManyField(Level) # Link with the levels of the school

	def __str__(self):
		return self.name


class Classroom(models.Model):
	""" Classroom model, it always refer to at least on profile """
	
	level = models.ForeignKey('Level') # Level or degree of the class (ex: 1ere)
	school = models.ForeignKey('School') # School witch the classroom belongs to
	name = models.CharField(max_length=100) # Name of the classroom (ex: Première S-3)
	shortName = models.CharField(max_length=8) # Name of the classroom shortened (ex: 1-S3)
	lessons = models.ManyToManyField(Lesson)

	def __str__(self):
		return self.name


class Profile(models.Model):
	""" Abstract User profile, it extends the original User class
		and is made to become weather a student or a teacher etc.. """
	
	user = models.OneToOneField(User) # Link with the original user class that we extend
	classroom = models.ForeignKey('Classroom') # Link to the user's classroom
	school = models.ForeignKey('School') # Link to the school of the profile (student or teacher)
	# I will add some other things but now this is it

	class Meta(object):
		abstract = True


class Student(Profile):			
	""" Student model, it exxtends the abstract Profile and the User
		model """

	isDelegate = models.BooleanField(default=False) # If the student is authorized to manage the classroom
	lessons = models.ManyToManyField(Lesson)

	def __str__(self):
		return "Profil de {0}".format(self.user.username)


class Teacher(models.Model):
	""" Teacher model, it does not extends the profile abstract but
		might do in the future if some want to connect to refiche """

	lastName = models.CharField(max_length=60) # Last name of the teacher
	firstName = models.CharField(max_length=30) # First name of the teacher

	def __str__(self):
		return self.lastName

class Sheet(models.Model):
	""" Sheet model (card, notes about a lesson etc) """

	name = models.CharField(max_length=50)
	sheetFile = models.FileField(upload_to=renameFile)
	uploadedBy = models.ForeignKey(Student)
	lesson = models.ForeignKey('Lesson')

	def __str__(self):
		return self.name