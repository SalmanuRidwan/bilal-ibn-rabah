from django.shortcuts import render
from .models import Class, Student

def CLASSES(request):
    classes = Class.objects.all()
    context = {'classes':classes}
    return render(request, 'classes.html', context)

def students(request):
    students = Student.objects.all()
    context = {'students':students}
    return render(request, 'students.html', context)

def class_detail(request, class_id):
    class_obj = Class.objects.get(pk=class_id)
    students = Student.objects.filter(classroom=class_obj)
    context = {
        'class_obj': class_obj,
        'students': students,
    }
    return render(request, 'class_detail.html', context)

def student_detail(request, student_id):
    student = Student.objects.get(id=student_id)
    context = {'student':student}
    return render(request, 'student_detail.html', context)