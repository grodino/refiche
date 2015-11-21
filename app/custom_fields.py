from django import forms
from os.path import splitext


class MultiFileInput(forms.FileInput):
	def render(self, name, value, attrs={}):
		attrs['multiple'] = 'multiple'
		return super(MultiFileInput, self).render(name, None, attrs=attrs)

	def value_from_datadict(self, data, files, name):
		if hasattr(files, 'getlist'):
			return files.getlist(name)
		elif hasattr(files, 'get'):
			return [files.get(name)]
		else:
			return files


class MultiFileField(forms.FileField):
	widget = MultiFileInput
	default_error_messages = {
		'min_num': u"Ensure at least %(min_num)s files are uploaded (received %(num_files)s).",
		'max_num': u"Ensure at most %(max_num)s files are uploaded (received %(num_files)s).",
		'file_size': u"File: %(uploaded_file_name)s, exceeded maximum upload size.",
		'file_extension': u"File: %(uploaded_file_name)s has a non-permitted extension %(uploaded_file_extension)s"
	}

	def __init__(self, *args, **kwargs):
		self.min_num = kwargs.pop('min_num', 0)
		self.max_num = kwargs.pop('max_num', None)
		self.maximum_file_size = kwargs.pop('maximum_file_size', None)
		self.allowed_extensions = kwargs.pop('allowed_extensions', None)

		super(MultiFileField, self).__init__(*args, **kwargs)


	def to_python(self, data):
		ret = []
		for item in data:
			ret.append(super(MultiFileField, self).to_python(item))
		return ret


	def validate(self, data):
		super(MultiFileField, self).validate(data)
		num_files = len(data)
		if len(data) and not data[0]:
			num_files = 0
		if num_files < self.min_num:
			raise forms.ValidationError(self.error_messages['min_num'] % {'min_num': self.min_num, 'num_files': num_files})
		elif self.max_num and num_files > self.max_num:
			raise forms.ValidationError(self.error_messages['max_num'] % {'max_num': self.max_num, 'num_files': num_files})
		for uploaded_file in data:
			file_extension = splitext(uploaded_file.name)[1]

			if uploaded_file.size > self.maximum_file_size:
				raise forms.ValidationError(self.error_messages['file_size'] % {'uploaded_file_name': uploaded_file.name})

			if file_extension not in self.allowed_extensions:
				raise forms.ValidationError(
					self.error_messages['file_extension'] % {
						'uploaded_file_name': uploaded_file.name,
						'uploaded_file_extension': file_extension
					}
				)