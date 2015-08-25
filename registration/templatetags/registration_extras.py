from django import template
from registration.forms import StudentCodeForm

register = template.Library()

@register.inclusion_tag('registration/newCode.html')
def getStudentRegistrationForm(request):
	""" Get the form for the generation of a code """

	form = StudentCodeForm()

	return {'form': form }