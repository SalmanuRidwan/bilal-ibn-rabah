from django.db import models
from django.urls import reverse

class Class(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self) -> str: return self.name


    class Meta:
        verbose_name_plural = 'classes'
        ordering = ['name']


class Parent(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone_number = models.CharField(max_length=11)


    def __str__(self) -> str: return self.name


    class Meta:
        ordering = ['name']


class Student(models.Model):
    name = models.CharField(max_length=100)
    reg_number = models.CharField(max_length=100)
    picture = models.ImageField('students/', default='avatar.png')
    classroom = models.ForeignKey(Class, on_delete=models.CASCADE)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)

    def __str__(self) -> str: return self.name

    def get_admin_edit_url(self):
        return reverse('admin:students_student_change', args=[str(self.pk)])

    class Meta:
        ordering = ['name']
