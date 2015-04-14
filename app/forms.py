from django import forms
from app.models import Sheet, Student

class UploadSheetForm(forms.ModelForm):
	def __init__(self, student, *args, **kwargs):
		super(UploadSheetForm, self).__init__(*args, **kwargs)
		self.fields['lesson'] = forms.ModelChoiceField(queryset=student.lessons.all())

	class Meta:
		model = Sheet
		exclude = ('uploadedBy',)
