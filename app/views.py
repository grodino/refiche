# coding=UTF-8
import json
from os.path import splitext
from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from app.models import Lesson, Sheet, Classroom, Student
from app.forms import UploadSheetForm
from app.functions import getStudent
from registration.models import StudentRegistrationCode
# _____________________________________________________________________
# VIEWS

@login_required
def home(request):
	""" App index view """

	student = getStudent(request.user)
	classroom = student.classroom
	lessons = classroom.lessons.all()

	# Construct the menu for the delegate
	if request.user.has_perm('registration.add_studentregistrationcode'):
		try:
			code = StudentRegistrationCode.objects.get(classroom=student.classroom).code
		except StudentRegistrationCode.DoesNotExist:
			code = 'NONE'

	return render(request, 'home.html', locals())


def underConstruction(request, classroom_name):
	""" A funny under construction page, just for fun """

	return render(request, 'app/under_construction.html', locals())


@login_required
def lessonPage(request, lesson_name):
	""" App lesson view, using the variable given it fetches 
		the lesson and all it's components """
	
	student = getStudent(request.user)
	
	try:
		lesson = student.classroom.lessons.get(name=lesson_name)
	except Lesson.DoesNotExist:
		raise Http404("This lesson does not exist or you are not registered to it !")

	sheets = Sheet.objects.filter(lesson=lesson).order_by('-uploadDate')

	return render(request, 'app/lesson.html', locals())


@login_required
def classroomPage(request):
	""" View to display informations about the classroom 
		like the students, the teachers, the school and so on """

	# TODO: If the student is delegate, allow him to modify stuff like delete students or name of the classroom
	student = getStudent(request.user)
	classroom = student.classroom

	# Get the Users who are in the classroom and who are part of the group delegates
	delegatesGroup = Group.objects.filter(name='delegates')
	delegates = Student.objects.filter(classroom=classroom,
									   user__groups=delegatesGroup)

	numberOfStudents = Student.objects.filter(classroom=classroom).count()
	numberOfLessons = classroom.lessons.all().count()

	return render(request, 'app/classroom.html', locals())


@login_required
def newSheetPage(request):
	""" NewSheet view to show the UploadSheetForm """

	student = getStudent(request.user)

	if request.method == "POST":
		form = UploadSheetForm(student=student, data=request.POST, files=request.FILES)
		
		if form.is_valid():
			sheet = form.save(commit=False)
			sheet.uploadedBy = student
			sheet.contentType = form.cleaned_data['sheetFile'].content_type
			sheet.name = splitext(form.cleaned_data['sheetFile'].name)[0]
			sheet.extension = splitext(form.cleaned_data['sheetFile'].name)[1]
			sheet.sheetType = form.cleaned_data['sheetType']
			sheet.save()

			localVarsJSON = json.dumps({'sucess': 'true',})
			messages.add_message(request, messages.SUCCESS, 'Votre fiche a bien été envoyée !')

			return HttpResponse(localVarsJSON, content_type='application/json')
		else:
			localVarsJSON = json.dumps(form.errors)
	else:
		raise Http404('Hey :/ I wasn\'t expecting you here !')

	return HttpResponse(localVarsJSON, content_type='application/json')


@login_required
def downloadSheetPage(request, pk):
	""" View for dowloading a sheet """

	student = getStudent(request.user)

	# Get the file
	try:
		sheet = Sheet.objects.get(pk=pk)
	except Sheet.DoesNotExist:
		raise Http404("Sorry this file does not exist :(")
	
	# Check if the user can have access to it (if he is part of the lesson)
	if sheet.lesson not in student.lessons.all():
		raise PermissionDenied()

	data = sheet.sheetFile.read()

	response = HttpResponse(data, content_type=sheet.contentType)
	response['Content-Disposition'] = 'attachment; filename="{}"'.format(sheet.name+sheet.extension)

	return response