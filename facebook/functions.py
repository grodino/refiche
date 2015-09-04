import random, string


def generateRandomKey(length=20):
	""" Creates a random key of the length given and returns it  """

	return ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(length))