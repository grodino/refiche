#coding=UTF-8
from os.path import splitext
from django import forms
from django.conf import settings
from app.models import Sheet, Lesson, Teacher

class UploadSheetForm(forms.ModelForm):
	def __init__(self, student, *args, **kwargs):
		super(UploadSheetForm, self).__init__(*args, **kwargs)
		self.fields['lesson'] = forms.ModelChoiceField(queryset=student.classroom.lessons.all(), label="Matière", empty_label=None)

	def clean_sheetFile(self):
		sheet = self.cleaned_data['sheetFile']
		sheetSize = sheet.size
		sheetExtension = splitext(sheet.name)[1]

		if sheetExtension not in settings.ALLOWED_EXTENSIONS:
			raise forms.ValidationError("Argh je ne digère pas ce format de fichier :(  [%(extension)s]",params={'extension': sheetExtension}, code='wrongFileExtension')
		elif sheetSize > settings.MAX_SHEET_SIZE:
			raise forms.ValidationError("Argh le fichier est trop gros :( [%(size)o octets]",params={'size': sheetSize}, code='fileToBig')
		

		return self.cleaned_data['sheetFile']

	class Meta:
		model = Sheet
		exclude = ('name', 'chapter', 'extension', 'uploadedBy', 'contentType', 'uploadDate')
