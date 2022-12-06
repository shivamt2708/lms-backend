from django.db import models

# Create your models here.
class Teacher(models.Model):
	full_name=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	password=models.CharField(max_length=100)
	qualification=models.CharField(max_length=100)
	mobile_no=models.CharField(max_length=100)
	address=models.TextField()

	class Meta:
		verbose_name_plural="1. Teachers"

class CourseCategory(models.Model):
	title=models.CharField(max_length=100)
	description=models.TextField()\

	class Meta:
		verbose_name_plural="2. Course Categories"

class Course(models.Model):
	category=models.ForeignKey(CourseCategory, on_delete=models.CASCADE)
	teacher=models.ForeignKey(Teacher, on_delete=models.CASCADE)
	title=models.CharField(max_length=100)
	description=models.TextField()
	techs=models.TextField(null=True)

	class Meta:
		verbose_name_plural="3. Courses"

	def related_videos (self):
		related_videos=Course.objects.filter(techs_icontains=self.techs).exclude(id=self.id)
		return serializers.serialize('json', related_videos)
	def tech_list(self):
		tech_list=self.techs
		return tech_list

class Student(models.Model):
	full_name=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	password=models.CharField(max_length=100)
	qualification=models.CharField(max_length=100)
	mobile_no=models.CharField(max_length=100)
	address=models.TextField()
	interested_categories=models.TextField()

	class Meta:
		verbose_name_plural="4. Students"

class Notification(models.Model):
	teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE,null=True)
	student=models.ForeignKey(Student,on_delete=models.CASCADE,null=True)
	notif_for=models.CharField(max_length=100,verbose_name='Notification for',null=True)
	notif_subject=models.CharField(max_length=100,verbose_name='Notification subject',null=True)
	notif_created_time=models.DateTimeField(auto_now_add=True)
	notifiread_status=models.BooleanField(default=True)

	class Meta:
		verbose_name_plural="5. Notifications"

class Contact(models.Model):
	full_name=models.CharField(max_length=100)
	email=models.EmailField()
	query_txt=models.TextField()
	add_time=models.DateTimeField(auto_now_add=True)

	def __str__(self) -> str:
		return self.query_txt

	class Meta:
		verbose_name_plural="6. Contact Queries"

class FAQ(models.Model):
	question=models.CharField(max_length=100)
	answer=models.TextField()

	def __str__(self) -> str:
		return self.question

	class Meta:
		verbose_name_plural="7. Faq"

class Chapter (models.Model):
	course=models.ForeignKey(Course,on_delete=models.CASCADE, related_name='course_chapters')
	title=models.CharField(max_length=150)
	description=models. TextField()
	video=models.FileField(upload_to='chapter_videos/', null=True)
	remarks=models.TextField(null=True)

	class Meta:
		verbose_name_plural="8. Chapters"

	def chapter_duration( self):
		seconds=0
		import cv2
		cap = cv2. VideoCapture(self.video.path)
		fps = cap.get (cv2.CAP_PROP_FPS)
	# OpenCV2 version 2 used "CV CAP PROP FPS"
		frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
		if frame_count:
			duration = frame_count/fps
			print('fps =' + str(fps))
			print ('number of frames ='+ str(frame_count))
			print ('duration (S) ='+ str(duration))
			minutes = int (duration/60)
			seconds = duration%60
			print('duration (M:S) =' +str(minutes) + ':' + str(seconds))
			return seconds

class StudentCourseEnrollment(models.Model):
	course=models.ForeignKey(Course, on_delete=models.CASCADE,related_name='enrolled_courses')
	student=models.ForeignKey(Student, on_delete=models.CASCADE,related_name='enrolled_student')
	enrolled_time=models.DateTimeField(auto_now_add=True)
	class Meta:
		verbose_name_plural="9. Enrolled Courses"
	def __str__(self):
		return f"{self.course} - {self.student}"

class CourseRating (models.Model) :
	course=models.ForeignKey(Course, on_delete=models. CASCADE)
	student=models.ForeignKey(Student, on_delete=models. CASCADE)
	rating=models.PositiveBigIntegerField(default=0)
	reviews=models.TextField(null=True)
	review_time=models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural="10. Course Ratings"

	def __str__(self):
		return f"{self.course} - {self.student} - {self.rating}"