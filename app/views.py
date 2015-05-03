from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import json
from django.core.exceptions import PermissionDenied
from app.models import Lesson, School, Sheet
from app.forms import UploadSheetForm
from app.functions import getStudent

# _____________________________________________________________________
# VIEWS

@login_required
def home(request):
	""" App index view """

	student = getStudent(request)
	lessons = student.lessons.all()
	classroom = student.classroom

	return render(request, 'home.html', locals())


@login_required
def lessonPage(request, lesson_name):
	""" App lesson view, using the variable given it fetches 
		the lesson and all it's components """
	
	student = getStudent(request)
	
	try:
		lesson = student.lessons.get(name=lesson_name)
	except Lesson.DoesNotExist:
		raise Http404("This lesson does not exist or you are not registered to it !")

	sheets = Sheet.objects.filter(lesson=lesson)

	return render(request, 'app/lesson.html', locals())


@login_required
def newSheetPage(request):
	""" NewSheet view to show the UploadSheetForm """

	student = getStudent(request)

	if request.method == "POST":
		form = UploadSheetForm(student=student, data=request.POST, files=request.FILES)
		
		if form.is_valid():
			sheet = form.save(commit=False)
			sheet.uploadedBy = student
			sheet.contentType = form.cleaned_data['sheetFile'].content_type
			sheetType = form.cleaned_data['sheetType']
			sheet.save()

			localVarsJSON = json.dumps({'sucess': 'Votre fichier a bien été envoyée',})

			return HttpResponse(localVarsJSON, content_type='application/json')
		else:
			localVarsJSON = json.dumps(form.errors)
	else:
		raise Http404('Hey :/ I wasn\'t expecting you here !')

	return HttpResponse(localVarsJSON, content_type='application/json')


@login_required
def downloadSheetPage(request, pk):
	""" View for dowloading a sheet """

	student = getStudent(request)

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
	response['Content-Disposition'] = 'attachment; filename="test.jpg"'

	return response