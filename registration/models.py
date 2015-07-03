from django.db import models
from app.models import Classroom


class StudentRegistrationCode(models.Model):
	""" Model for a code made to be  given to students for them to sign up """

	code = models.CharField(unique=True,
							max_length=20)
	classroom = models.OneToOneField(Classroom)
	numberOfStudents = models.IntegerField(verbose_name='nombre d\'élèves')
	numberOfStudentsLeft = models.IntegerField(verbose_name='nombre d\'élèves restants')

	def __str__(self):
		return '{} pour {} élèves de {}'.format(self.code, self.numberOfStudents, self.classroom)
