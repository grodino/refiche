# coding=UTF-8
from django.contrib.auth import signals
import logging

def userConnected(**kwargs): # When Django tells me that a user has connected I write it in the log
	user = kwargs['user'].username.upper()
	logger = logging.getLogger('users')
	logger.info('User '+user+' has connected !')

def userDisconnected(**kwargs): # When Django tells me that a user has disconnected I write it in the log
	user = kwargs['user'].username.upper()
	logger = logging.getLogger('users')
	logger.info('User '+user+' has disconnected !')

logger = logging.getLogger('django')
signals.user_logged_in.connect(userConnected) # I ask Django to look for any user login
signals.user_logged_out.connect(userDisconnected) # I ask Django to look for any user logout
