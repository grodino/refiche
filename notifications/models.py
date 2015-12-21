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

	defaultTemplate= 'notifications/basic_notification.html'
	instance = None

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
		from app.models import Sheet

		user = self.receiver
		content = self.content

		# TODO: Create text only template, create a template for Links
		# TODO: Fix the media serving with nginx (allow anyone to access to sheet and link thumbnails) and in DEBUG

		if self.content:
			subject = """ Vous avez une nouvelle notification! """

			context = locals()
			template = get_template(self.defaultTemplate).render(context)
		elif self.sender == 'Sheet':
			subject = """ De nouvelles fiches vous attendent! """
			sheet = self.instance

			print('DEBUG', sheet.name)

			context = locals()
			template = get_template('notifications/sheet_notification.html').render(context)
			self.content = """ Salut envoie moi un mail si tu ne vois que ça, il faut que je règle ce problème ! """ # TODO: Use the template for text only email
		else:
			subject = """ Vous avez une nouvelle notification! """

			context = locals()
			template = get_template(self.defaultTemplate).render(context)
			self.content = """ Vous avez une nouvelle notification! """ # TODO: Use the template for text only email


		user.email_user(
			subject=subject,
			message='',
			html_message=template,
			from_email='contact@refiche.fr'
		)


class NotificationManager(object):
	"""
	Class made to provide some functions to notify groups
	like a school, a classroom etc
	"""

	def notifyClassroom(self, classroom, sender, instance=None, content=None):
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

			notification.instance = instance

			notification.notifyAndSave()






















