from django.urls import path
from . import views

urlpatterns = [
    path('teacher/', views.TeacherList.as_view()),
    path('pages/', views.FlatPagesList.as_view()),
    path('pages/<int:pk>/<str:page_slug>/', views.FlatPagesDetail.as_view()),
    path('contact/', views.ContactList.as_view()),
    path('faq/', views.FaqList.as_view()),
    path( 'category/', views. CategoryList.as_view()),
    # Course
    path('course/',views. CourseList.as_view()),
    # Course Detail
    path('course/<int:pk>/', views.CourseDetailView.as_view()),
    # Specific Course Chapter
    path('course-chapters/<int:course_id>',views.CourseChapterList.as_view() ),
    # Specific Chapter
    path ('chapter/<int:pk>', views.ChapterDetailView.as_view()),
    # Teacher Courses
    path('teacher-courses/<int:teacher_id>', views.TeacherCourseList.as_view()),
    # Course Detail
    path( 'teacher-course-detail/<int:pk>', views.TeacherCourseDetail.as_view()),
    # Student
    path('student/', views. StudentList.as_view()),
    
    path('student-enroll-course/', views. StudentEnrollCourseList.as_view()),
    path('fetch-enroll-status/<int:student_id>/<int:course_id>', views.fetch_enroll_status),
    path('fetch-enrolled-students/<int:course_id>',views. EnrolledStudentList.as_view() ),
    path ('course-rating/', views. CourseRatingList.as_view()),
    path('fetch-rating-status/<int:student_id>/<int:course_id>', views.fetch_rating_status),



]
