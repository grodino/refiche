from django.contrib.auth.models import User

from app.models import Student


class FacebookBackend(object):
	"""
	A login backend to login users with facebook
	"""

	def authenticate(self, fb_id=None):
		"""
		Checks if the user_facebook_id is known by the database
		"""

		print('HELLLLO !')
		try:
			student = Student.objects.get(facebookId=fb_id)
			user = student.user
		except Student.DoesNotExist:
			return None

		return user


	def get_user(self, user_id):
		"""
		Gets a User object with the user_id (the pk of the user)
		"""

		print('HELLLLO !')
		try:
			return User.objects.get(pk=user_id)
		except User.DoesNotExist:
			return None