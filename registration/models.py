from django.db import models


class StudentRegistrationCode(models.Model):
	""" Model for a code made to be  given to students for them to sign up """

	code = models.CharField(max_length=20)
	numberOfStudents = models.IntegerField(verbose_name='nombre d\'élèves')

	def __str__(self):
		return '{} pour {} élèves'.format(self.code, self.numberOfStudents)
