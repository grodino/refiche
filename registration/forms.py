from django import forms
from django.contrib.auth.models import User

class StudentRegistrationForm(forms.Form):
	code = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'full-container-width'}))

class DelegateRegistrationForm(forms.ModelForm):
	class Meta:
		model = User
		exclude = ('email',)