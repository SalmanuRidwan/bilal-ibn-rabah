from django.contrib import admin
from .models import Parent, Class, Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'reg_number', 'student_class', 'student_parent']

admin.site.register(Student, StudentAdmin)
admin.site.register(Parent)
admin.site.register(Class)