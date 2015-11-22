#coding=UTF-8
from os.path import splitext
from django import forms
from django.conf import settings
from app.models import Sheet, Link
from app.custom_fields import MultiFileField

class UploadSheetForm(forms.ModelForm):
	def __init__(self, student, *args, **kwargs):
		super(UploadSheetForm, self).__init__(*args, **kwargs)
		self.fields['lesson'] = forms.ModelChoiceField(
			queryset=student.classroom.lessons.all(),
			label="Matière",
			empty_label=None
		)

	class Meta:
		model = Sheet
		exclude = ('chapter', 'uploadedBy', 'uploadDate', 'extension', 'contentType', 'thumbnail')

		widgets = {
			'name': forms.TextInput(attrs={'readonly': 'readonly', 'placeholder': 'Sélectionnez le fichier'})
		}


class UploadFileForm(forms.Form):
	file = MultiFileField(
		max_num=15,
		min_num=1,
		maximum_file_size=settings.MAX_SHEET_SIZE,
		allowed_extensions=settings.ALLOWED_EXTENSIONS,
		label='Fichier(s)'
	)


class UploadLinkForm(forms.ModelForm):
	def __init__(self, student, *args, **kwargs):
		super(UploadLinkForm, self).__init__(*args, **kwargs)
		self.fields['lesson'] = forms.ModelChoiceField(
			queryset=student.classroom.lessons.all(),
			label="Matière",
			empty_label=None,
			widget=forms.Select(attrs={'class': 'full-container-width'})
		)


	class Meta:
		model = Link
		exclude = ('chapter', 'uploadedBy', 'uploadDate', 'webSiteName', 'thumbnail')

		widgets = {
			'url': forms.TextInput(attrs={
				'class': 'full-container-width',
				'placeholder': 'ex: http://refiche.fr'})
		}