from django.contrib import admin

# Register your models here.
from .import models

admin.site.register(models.Teacher)
admin.site.register(models.CourseCategory)
admin.site.register(models.Course)
admin.site.register(models.Student)

class NotificationAdmin(admin.ModelAdmin):
	list_display=['id','notif_for','notif_subject','notifiread_status']
admin.site.register(models.Notification,NotificationAdmin)

admin.site.register(models.Contact)
admin.site.register(models.FAQ)

admin.site.register(models.Chapter)

admin.site.register(models.StudentCourseEnrollment)


admin.site.register(models.CourseRating)