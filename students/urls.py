from django.urls import path

from .views import CLASSES, students, class_detail, student_detail

urlpatterns = [
    path('', CLASSES, name='classes'),
    path('class/<int:class_id>/', class_detail, name='class_detail'),
    path('student/<int:student_id>/', student_detail, name='student_detail'),
    path('students/', students, name='students'),
]
