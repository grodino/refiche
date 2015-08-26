from os.path import splitext
from django import forms
from django.conf import settings
from app.models import School, Level
from registration.models import StudentRegistrationCode


class StudentCodeForm(forms.ModelForm):
	class Meta:
		model = StudentRegistrationCode
		fields = ('numberOfStudents',)
		widgets = {
			'numberOfStudents': forms.NumberInput(attrs={'min': '1', 'class': 'full-container-width'})
		}

	def clean_numberOfStudents(self):
		if self.cleaned_data.get('numberOfStudents') <= 0:
			raise forms.ValidationError('Vous ne pouvez pas inscrire un nombre nul ou négatif d\'élèves :/',
										code='not_positive')

		return self.cleaned_data.get('numberOfStudents')


class StudentRegistrationForm(forms.Form):
	code = forms.CharField(max_length=20,
						   label='Code d\'inscription')


class RegistrationForm(forms.Form):
	""" Basic form for registration, it is generic to be inherited """

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
	avatar = forms.FileField(label='Photo de profil (facultatif)',
							 required=False)

	def clean_password2(self):
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')

		if password1 and password2 and password1 != password2:
			raise forms.ValidationError('Les deux mots de passe ne correspondent pas',
										code='password_mismatch',)

		return password2


	def clean_avatar(self):
		ALLOWED_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.gif')

		avatar = self.cleaned_data['avatar']

		if avatar == None:
			return avatar

		avatarExtension = splitext(avatar.name)[1]
		avatarSize = avatar.size

		if avatarExtension not in ALLOWED_EXTENSIONS:
			raise forms.ValidationError('Les photos dont le format de fichier est en'+avatarExtension+' ne sont pas acceptées :/',
										 code='wrong_extension')
		elif avatarSize > settings.MAX_PICTURE_SIZE:
			raise forms.ValidationError("Argh le fichier est trop gros :( [%(size)o octets]",
										params={'size': avatarSize},
										code='to_big_picture')

		return avatar




class DelegateRegistrationForm(RegistrationForm):
	""" Extends the basic form and adds the classroom creation ability for delegates"""

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
