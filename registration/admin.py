from django.contrib import admin
from registration.models import StudentRegistrationCode


@admin.register(StudentRegistrationCode)
class SheetAdmin(admin.ModelAdmin):
	list_display = ('code', 'numberOfStudents',)