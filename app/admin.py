# coding=UTF-8
from django.contrib import admin
from app.models import Student, Classroom, School, Level, Teacher, Lesson, Sheet, Chapter

class SheetAdmin(admin.ModelAdmin):
	list_display = ('name', 'extension', 'uploadedBy', 'chapter', 'lesson', 'uploadDate', 'contentType')
	list_filter = ('uploadedBy','uploadDate')

class StudentAdmin(admin.ModelAdmin):
	list_display = ('user', 'classroom', 'school', 'isDelegate')
	list_filter = ('school',)

class TeacherAdmin(admin.ModelAdmin):
	list_display = ('lastName', 'gender')

class LessonAdmin(admin.ModelAdmin):
	list_display = ('name', 'teacher')
	list_filter = ('teacher',)

admin.site.register(Sheet, SheetAdmin)
admin.site.register(Chapter)
admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Classroom)
admin.site.register(School)
admin.site.register(Level)
admin.site.register(Lesson, LessonAdmin)
