from django.db import models


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
    classroom = models.ForeignKey(Class, on_delete=models.CASCADE)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)

    def __str__(self) -> str: return self.name

    class Meta:
        ordering = ['name']