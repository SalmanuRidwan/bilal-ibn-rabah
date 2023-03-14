from django.shortcuts import render
from .models import Class, Student
from django.shortcuts import get_object_or_404

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


def search_student(request):
    if request.method == 'GET':
        search_query = request.GET.get('q')
        if search_query:
            results = Student.objects.filter(name__icontains=search_query)
            return render(request, 'search_student.html', {'results': results})
    return render(request, 'search_student.html')
