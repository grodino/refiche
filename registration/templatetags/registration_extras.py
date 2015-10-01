from django import template
from django.contrib.auth.forms import PasswordChangeForm
from app.functions import getStudent
from registration.forms import StudentCodeForm, ChangeUserInfosForm

register = template.Library()

@register.inclusion_tag('registration/newCode.html')
def getStudentRegistrationForm(request):
	""" Get the form for the generation of a code """

	form = StudentCodeForm()

	return {'form': form }



@register.inclusion_tag('registration/change_user_infos.html')
def getStudentAccountForm(request):
	""" Get the managing account form and adds the context """

	student = getStudent(request.user)

	form = ChangeUserInfosForm()
	passwordForm = PasswordChangeForm(request.user)

	return locals()