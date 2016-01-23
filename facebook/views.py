import json
from django.http import Http404, HttpResponse
from app.functions import getStudent
from facebook.models import CreateGroupToken, ClassGroup

def createClassroomGroup(request, tokenValue, facebookUserId):
	""" Creates a classroom group for the user that claimed it
	 	/!\ The user is fetched by the token, that's why there is not decorator"""

	# Check if the token exists
	try:
		token = CreateGroupToken.objects.get(value=tokenValue)
	except CreateGroupToken.DoesNotExist:
		raise Http404('Votre token n\'existe pas !')

	student = getStudent(token.delegate)
	classroom = student.classroom

	fbGroup = ClassGroup()
	fbGroup.groupId = fbGroup.createClassGroup(student, facebookUserId)
	fbGroup.name = classroom.name
	fbGroup.save()

	token.delete()

	return HttpResponse(
		json.dumps({'success': True,
					'id': fbGroup.groupId}),
		content_type='application/json'
	)