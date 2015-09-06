import requests
from django.db import models
from django.http import Http404
from django.conf import settings
from django.contrib.auth.models import User
from facebook.functions import generateRandomKey


class CreateGroupToken(models.Model):
	""" Token generated when a delegate registers and allows him to create a ClassGroup """

	value = models.CharField(max_length=20, unique=True, default=generateRandomKey)
	delegate = models.OneToOneField(User)

	def __str__(self):
		return "{} par {}".format(self.value, self.delegate)


class FacebookAPIConnexion(models.Model):
	""" Class made to handle the connexion with facebook
		it has methods and variables to help it """

	appSecret = settings.FACEBOOK_APP_SECRET
	appId = settings.FACEBOOK_APP_ID
	facebookApiUrl = 'https://graph.facebook.com'

	class Meta(object):
		abstract = True

	@property
	def appToken(self):
		""" Get the facebook app token needed to for app group creation for example """

		r = requests.get(
			self.facebookApiUrl+'/oauth/access_token',
			params={'client_id': self.appId,
					'client_secret': self.appSecret,
					'grant_type': 'client_credentials'}
		)

		status = r.status_code # If it's a bad request (if facebook is down mostly)

		if status >= 400:
			raise Http404('Je n\'arrive pas à parler avec Facebook :/ la connexion passe mal :\'(')
		else:
			response = r.text.replace('access_token=', '')

		return response


class ClassGroup(FacebookAPIConnexion):
	""" Model made to make a connection between the Classroom model and the facebook group
	 	It is not required """

	groupId = models.CharField(max_length=50, unique=True)
	name = models.CharField(max_length=50)

	@classmethod
	def createClassGroup(self, student, uid=None):
		""" Create the facebook group of the class and make the student passed in argument the admin """

		if uid is None:
			uid = student.facebookId

		r = requests.post(
			self.facebookApiUrl+'/'+str(self.appId)+'/groups',
			data={'name': student.classroom.name,
				  'description': 'Le groupe de classe de la '+student.classroom.name,
				  'privacy': 'closed',
				  'admin': uid,
				  'access_token': str(self.appToken.fget(self))}
		)

		status = r.status_code

		if status >= 400:
			print(r.text)
			raise Http404('Je n\'arrive pas à parler avec Facebook :/ la connexion passe mal :\'(')

		return r.text.replace('{"id":"', '').replace('"}', '')

	def __str__(self):
		return self.groupId
