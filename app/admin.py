# coding=UTF-8
from django.contrib import admin
from app.functions import getStudent
from app.models import Student, Classroom, School, Level, Teacher, Lesson, Sheet, Chapter, Link


@admin.register(Sheet)
class SheetAdmin(admin.ModelAdmin):
	list_display = ('name', 'extension', 'uploadedBy', 'chapter', 'lesson', 'uploadDate', 'contentType')
	list_filter = ('uploadedBy','uploadDate')

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
	list_display = ('webSiteName', 'url', 'thumbnail', 'uploadedBy', 'chapter', 'lesson', 'uploadDate')
	list_filter = ('uploadedBy','uploadDate')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
	list_display = ('user', 'classroom', 'school')
	list_filter = ('school',)

	def get_queryset(self, request):
		qs = super(StudentAdmin, self).get_queryset(request)

		if request.user.is_superuser:
			return qs
		else:
			student = getStudent(request.user)
			return qs.filter(classroom=student.classroom)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
	list_display = ('lastName', 'gender', 'createdBy')
	search_fields = ['lastName']
	exclude = ('createdBy',)

	def get_queryset(self, request):
		qs = super(TeacherAdmin, self).get_queryset(request)

		if request.user.is_superuser:
			return qs
		else:
			student = getStudent(request.user)
			return qs.filter(createdBy=student)

	def save_model(self, request, obj, form, change):
		if request.user.is_superuser:
			if obj.createdBy is None:
				obj.createdBy = getStudent(request.user)
		else:
			obj.createdBy = getStudent(request.user)

		obj.save()

	def get_form(self, request, obj=None, **kwargs):
		if request.user.is_superuser:
			self.exclude = None

		return super(TeacherAdmin, self).get_form(request, obj, **kwargs)

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
	list_display = ('name', 'teacher')
	list_filter = ('teacher',)

	def get_queryset(self, request):
		qs = super(LessonAdmin, self).get_queryset(request)

		if request.user.is_superuser:
			return qs
		else:
			student = getStudent(request.user)
			return qs.filter(classroom=student.classroom)

	def save_model(self, request, obj, form, change):
		obj.save()

		if not request.user.is_superuser:
			student = getStudent(request.user)
			student.classroom.lessons.add(obj)

@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
	list_display = ('name', 'school', 'level')
	exclude = ('lessons', )

	def get_form(self, request, obj=None, **kwargs):
		if request.user.is_superuser:
			self.exclude = None

		return super(ClassroomAdmin, self).get_form(request, obj, **kwargs)

	def get_queryset(self, request):
		qs = super(ClassroomAdmin, self).get_queryset(request)

		if request.user.is_superuser:
			return qs
		else:
			student = getStudent(request.user)
			return qs.filter(id=student.classroom.id)


admin.site.register(Chapter)
admin.site.register(School)
admin.site.register(Level)
