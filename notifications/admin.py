from django.contrib import admin

from app.models import Student

from notifications.models import NotificationSettings, Notification

@admin.register(NotificationSettings)
class NotificationSettingsAdmin(admin.ModelAdmin):
	list_display = ('student', 'mailsEnabled', 'groupedMailsEnabled',)

	def student(self, obj):
		student = Student.objects.get(notificationsSettings=obj)

		return student

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
	list_display = ('sender', 'receiver', 'content', 'hasBeenRead', 'dateCreated')