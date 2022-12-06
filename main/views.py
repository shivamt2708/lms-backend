from django.shortcuts import render
from webbrowser import get
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import generics
from rest_framework import permissions
from django.contrib.flatpages.models import FlatPage
from .serializers import TeacherSerializer,FlatPagesSerializer,ContactSerializer,FAQSerializer,CategorySerializer,CourseSerializer,ChapterSerializer,StudentSerializer,StudentCourseEnrollSerializer,CourseRatingSerializer

from . import models


class TeacherList(generics.ListCreateAPIView):
	queryset=models.Teacher.objects.all()
	serializer_class = TeacherSerializer
	permissions_classes=[permissions.IsAuthenticated]

class TeacherDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset=models.Teacher.objects.all()
	serializer_class = TeacherSerializer
	permissions_classes=[permissions.IsAuthenticated]

@csrf_exempt
def teacher_login(request):
    email=request.POST['email']
    password=request.POST['password']

    teacherData=models.Teacher.objects.get(email=email,password=password)
    if teacherData:
        return JsonResponse({'bool':True})

    else:
        return JsonResponse({'bool':False})

class FlatPagesList(generics.ListCreateAPIView):
	queryset=FlatPage.objects.all()
	serializer_class = FlatPagesSerializer

class FlatPagesDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset=FlatPage.objects.all()
	serializer_class = FlatPagesSerializer

class ContactList(generics.ListCreateAPIView):
	queryset=models.Contact.objects.all()
	serializer_class = ContactSerializer

class FaqList(generics.ListCreateAPIView):
	queryset=models.FAQ.objects.all()
	serializer_class = FAQSerializer

class CategoryList(generics.ListCreateAPIView):
    queryset=models.CourseCategory.objects.all()
    serializer_class=CategorySerializer

# Course
class CourseList(generics.ListCreateAPIView):
    queryset = models.Course.objects.all()
    serializer_class = CourseSerializer
    def get_queryset(self):
        qs=super() .get_queryset()
        if  'result'  in self. request.GET:
            limit=int(self.request.GET[ 'result' ])
            qs=models.Course.objects.all().order_by('-id') [:limit]
        if 'category' in self.request.GET:
            category=self.request.GET['category']
            qs=models.Course.objects.filter(techs_icontains=category)
        if  'skill_name' in self. request.GET and 'teacher' in self.request.GET:
            skill_name=self. request.GET[ 'skill_name' ]
            teacher=self.request.GET['teacher']
            teacher=models.Teacher.obiects.filter(id=teacher).first()
            qs=models.Course.objects.filter(techs_icontains=skill_name, teacher=teacher)

        return qs
        
class CourseDetailView(generics.RetrieveAPIView):
    queryset=models.Course.objects.all()
    serializer_class=CourseSerializer
    
class TeacherCourseList(generics.ListCreateAPIView):
    serializer_class=CourseSerializer
    def get_queryset(self):
        teacher_id = self.kwargs['teacher_id']
        teacher = models.Teacher.objects.get (pk=teacher_id)
        return models.Course.objects.filter(teacher=teacher)

# Specific Teacher Course
class TeacherCourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.Course.objects.all()
    serializer_class=CourseSerializer
    
class CourseChapterList(generics.ListCreateAPIView):
    queryset=models.Chapter.objects.all()
    serializer_class = ChapterSerializer

    def get_queryset(self):
        course_id=self.kwargs[ 'course_id']
        course = models.Course.objects.get(pk=course_id)
        return  models. Chapter.objects.filter (course=course)
        
class ChapterDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.Chapter.objects.all()
    serializer_class=ChapterSerializer

class StudentList(generics.ListCreateAPIView):
    queryset=models.Student.objects.all()
    serializer_class=StudentSerializer
# permission classes=[permissions.IsAuthenticated]

def student_login(request):
    email=request.POST['email']
    password=request.POST['password']

    studentData=models.Student.objects.get(email=email,password=password)
    if studentData:
        return JsonResponse({'bool':True})

    else:
        return JsonResponse({'bool':False})

class StudentEnrollCourseList(generics.ListCreateAPIView):
    queryset=models.StudentCourseEnrollment.objects.all()
    serializer_class=StudentCourseEnrollSerializer

def fetch_enroll_status(request, student_id, course_id):
    student=models.Student.objects.filter(id=student_id).first()
    course=models.Course.objects.filter(id=course_id).first()
    enrollStatus=models.StudentCourseEnrollment.objects.filter(course=course,student=student).count()
    if enrollStatus:
        return JsonResponse({'bool': True})
    else:
        return JsonResponse({'bool': False})


class EnrolledStudentList(generics.ListAPIView):
    queryset=models.StudentCourseEnrollment.objects.all()
    serializer_class=StudentCourseEnrollSerializer
    def get_queryset(self):
        course_id=self.kwargs['course_id']
        course = models.Course.objects.get (pk=course_id)
        return models.StudentCourseEnrollment.objects.filter(course=course)

class CourseRatingList(generics.ListCreateAPIView):
    queryset=models.CourseRating.objects.all()
    serializer_class=CourseRatingSerializer
    
def fetch_rating_status (request, student_id, course_id):
    student=models.Student.objects.filter(id=student_id).first()
    course=models.Course.objects. filter(id=course_id).first()
    ratingStatus=models.CourseRating.objects.filter(course=course,student=student).count()
    if ratingStatus:
        return JsonResponse({'bool': True})
    else:
        return JsonResponse({'bool': False})