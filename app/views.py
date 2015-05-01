from django.shortcuts import render, redirect
import logging
from django.http import Http404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from app.models import Student, Lesson, School, Sheet
from app.forms import UploadSheetForm

# _____________________________________________________________________
# FUNCTIONS

def getStudent(request):
	""" /!\ Not a view, it fetches the user and verifiy if there
		is a profile account logged to it. RETURNS THE STUDENT """

	user = request.user
	
	try:
		student = Student.objects.get(user=user)
	except Student.DoesNotExist:
		logger = logging.getLogger('users')
		logger.error(user.username+'\'s account is not linked to a profile account! id = '+str(user.id))
		raise Http404("Your user account is not linked to a profile account !")

	return student

def renameFileForDown(instance):
	""" NOT A MODEL, it's a function made to modify the name 
		of the file like this it won't be executed """

	instance.name.replace('point-', '.')

	return name


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
			sheet.save()

			messages.add_message(request, messages.SUCCESS, 'Votre fichier a bien été envoyé !')
			return redirect('/app/home')
	else:
		form = UploadSheetForm(student=student)

	return render(request, 'app/newSheet.html', locals())

@login_required
def downloadSheetPage(request):
	""" View for dowloading a sheet """

	try:
		sheet = Sheet.objects.get(name='test')
	except Sheet.DoesNotExist:
		raise Http404("Sorry this file does not exist :(")
	data = sheet.sheetFile.read()

	response = HttpResponse(data, content_type=sheet.contentType)
	response['Content-Disposition'] = 'attachment; filename="test.jpg"'

	return response
