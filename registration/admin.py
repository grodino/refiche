from django.contrib import admin
from app.functions import getStudent
from registration.models import StudentRegistrationCode


@admin.register(StudentRegistrationCode)
class CodeAdmin(admin.ModelAdmin):
	list_display = ('code', 'numberOfStudents', 'numberOfStudentsLeft')

	def get_queryset(self, request):
		qs = super(CodeAdmin, self).get_queryset(request)

		if request.user.is_superuser:
			return qs
		else:
			student = getStudent(request.user)
			return qs.filter(classroom=student.classroom)