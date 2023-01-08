from django.db import models

class Manager(models.Model):
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return  self.f_name

class Student(models.Model):
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    bio = models.TextField(null=True, blank=True)
    age = models.PositiveSmallIntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.f_name


class Teacher(models.Model):
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    bio = models.TextField(null=True, blank=True)
    age = models.PositiveSmallIntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.f_name

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    Teachers = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    Stdudents = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.title