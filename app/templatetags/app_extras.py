from django import template
from app.forms import UploadSheetForm
from app.functions import getStudent

register = template.Library()

@register.inclusion_tag('app/newSheet.html')
def getNewSheetForm(request):
	student = getStudent(request)
	form = UploadSheetForm(student=student)

	return {'form': form }