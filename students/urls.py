from django.urls import path

from .views import CLASSES, students, class_detail, student_detail, search_student

urlpatterns = [
    path('', CLASSES, name='classes'),
    path('classes/<int:class_id>/', class_detail, name='class_detail'),
    path('student/<int:student_id>/', student_detail, name='student_detail'),
    path('students/', students, name='students'),
    path('search/', search_student, name='search_student'),
]
