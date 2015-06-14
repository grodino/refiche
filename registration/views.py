from django.shortcuts import render
from django.contrib import messages
from registration.forms import StudentRegistrationForm, DelegateRegistrationForm

def register(request):
	""" View for signing up, also includes a form for the students who have a link """

	if request.method == 'POST':
		form = StudentRegistrationForm(request.POST)

		if form.is_valid():
			hello_g = form.cleaned_data['code']
			messages.add_message(request, messages.SUCCESS, 'MA couillle !!!')
	else:
		form = StudentRegistrationForm()

	return render(request, 'registration.html', locals())


def delegateRegister(request):
	""" View for registration by the delegate of the classroom """

	form = DelegateRegistrationForm()

	return render(request, 'registration/delegate_register.html', locals())