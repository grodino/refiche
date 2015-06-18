from datetime import timedelta
from django import template
from django.utils import timezone
from django.contrib.humanize.templatetags.humanize import naturaltime, naturalday
from app.forms import UploadSheetForm, LessonForm
from app.functions import getStudent

register = template.Library()

@register.inclusion_tag('app/newSheet.html')
def getNewSheetForm(request):
	"""
	:param request: the context of the template
	:return: the form with the user's data
	"""

	student = getStudent(request.user)
	form = UploadSheetForm(student=student)

	return {'form': form }


@register.inclusion_tag('app/newLesson.html')
def getLessonForm():
	""" Returns the LessonForm """

	form = LessonForm()
	return {'form': form }


@register.filter()
def naturaltime_addon(uploadDate):
	"""
	:param uploadDate: the date when the object was added
	:return: True if was more than 12 hours ago
	"""

	if timezone.now() > uploadDate + timedelta(days=1.1):
		return 'le {0}'.format(naturalday(uploadDate, 'd M Y'))
	elif timezone.now() > uploadDate + timedelta(hours=12):
		return naturalday(uploadDate)

	return naturaltime(uploadDate)