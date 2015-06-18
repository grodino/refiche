from django import forms
from app.models import School, Level

class StudentRegistrationForm(forms.Form):
	code = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'full-container-width'}))


class DelegateRegistrationForm(forms.Form):
	# Information about the delegate, will be stored in the User model
	firstName = forms.CharField(max_length=30,
								label='Prénom',
								widget=forms.TextInput(attrs={'required': True, 'placeholder': 'Ex: Jean', 'class': 'full-container-width'}))
	lastName = forms.CharField(max_length=30,
							   label='Nom',
							   widget=forms.TextInput(attrs={'required': True, 'placeholder': 'Ex: Dupond', 'class': 'full-container-width'}))
	password1 = forms.CharField(label='Mot de passe',
								widget=forms.PasswordInput(attrs={'required': True, 'placeholder': 'Tous les caractères sont autorisés', 'class': 'full-container-width'}))
	password2 = forms.CharField(label='Confirmation du mot de passe',
								widget=forms.PasswordInput(attrs={'required': True, 'class': 'full-container-width'}))
	email = forms.EmailField(max_length=100,
							 widget=forms.EmailInput(attrs={'required': True, 'placeholder': 'Ex: jdupond@email.fr', 'class': 'full-container-width'}))

	# Information about the classroom, will be stored in the corresponding models
	school = forms.ModelChoiceField(School.objects.all(),
									label='École',
									widget=forms.Select(attrs={'required': True, 'class': 'full-container-width'}),
									empty_label=None)
	classroomName = forms.CharField(max_length=100,
									label='Nom de la classe',
									widget=forms.TextInput(attrs={'required': True, 'placeholder': 'Ex: Première S3', 'class': 'full-container-width'}))
	classroomShortName = forms.CharField(max_length=100,
										 label='Nom court de la classe',
										 widget=forms.TextInput(attrs={'required': True, 'placeholder': 'Ex: 1-S3', 'class': 'full-container-width'}))
	classroomLevel = forms.ModelChoiceField(Level.objects.all(),
											label='Degré',
											widget=forms.Select(attrs={'required': True, 'class': 'full-container-width'}),
											empty_label=None)

	def clean_password2(self):
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')

		if password1 and password2 and password1 != password2:
			raise forms.ValidationError('Les deux mots de passe ne correspondent pas',
										code='password_mismatch',)

		return password2

	def clean_numberOfStudents(self):
		if self.cleaned_data.get('numberOfStudents') <= 0:
			raise forms.ValidationError('Vous ne pouvez pas avoir un nombre d\'élèves négatif ou nul dans une classe !',
										code='password_mismatch',)