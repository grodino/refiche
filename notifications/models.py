import asyncio

from django.db import models
from django.contrib.auth.models import User
from django.template.loader import get_template

from app.functions import getStudent


class NotificationSettings(models.Model):
	"""
	A model made to store the user's settings about notifications
	"""

	mailsEnabled = models.BooleanField()
	groupedMailsEnabled = models.BooleanField()

	def __str__(self):
		return 'mails: {}, grouped mails: {}'.format(self.mailsEnabled, self.groupedMailsEnabled)


class Notification(models.Model):
	"""
	Class for a notification made to be inherited to specify
	notification types. When a notification is notified,
	it is saved
	"""

	sender = models.CharField(max_length=50)
	receiver = models.ForeignKey(User)
	content = models.CharField(max_length=250)
	hasBeenRead = models.BooleanField(default=False)
	dateCreated = models.DateTimeField(auto_now_add=True, auto_now=False)

	templateDir = 'notifications/basic_notification.html'

	def __str__(self):
		return '{} to {}'.format(self.sender, self.receiver)

	def notifyAndSave(self):
		"""
		Check the user settings and then call the proper
		notification functions (emails, grouped emails etc)
		and save the notification
		"""

		student = getStudent(self.receiver)

		if student.notificationsSettings.mailsEnabled:
			self.__notifyMail()
		else:
			self.__notifyMail()

		self.save()

	def markAsRead(self):
		"""
		Mark a notification as read
		"""

		self.hasBeenRead = True

	def __notifyMail(self):
		"""
		Notify the user by mail for each notification
		"""

		user = self.receiver
		content = self.content

		if self.sender == 'AbstractUploadedContent':
			subject = """ De nouvelles fiches vous attendent! """
		else:
			subject = """ Vous avez une nouvelle notification! """

		context = locals()
		template = get_template(self.templateDir).render(context)

		user.email_user(
			subject,
			template,
			'contact@refiche.fr'
		)


class NotificationManager(object):
	"""
	Class made to provide some functions to notify groups
	like a school, a classroom etc
	"""

	def notifyClassroom(self, classroom, sender, content):
		"""
		Notify create a notification for each student of a classroom
		and notify him
		"""
		from app.models import Student

		students = Student.objects.filter(classroom=classroom)

		for student in students:
			notification = Notification()
			notification.sender = sender.__name__
			notification.receiver = student.user
			notification.content = content
			notification.notifyAndSave()






















