from django import template
from registration.forms import StudentRegistrationForm

register = template.Library()

@register.inclusion_tag('registration/newCode.html')
def getStudentRegistrationForm(request):
	""" Get the form for the generation of a code """

	form = StudentRegistrationForm()

	return {'form': form }