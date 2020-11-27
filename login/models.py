from django.db import models

# Create your models here.
"""
Databases:
    1. Admin
    2. Professor
    3. Student
    4. FacultyAdvisor
"""


class Admin(models.Model):
    name = models.CharField(max_length=40)
    username = models.CharField(max_length=40, unique=True, primary_key=True)
    password = models.CharField(max_length=40)

    def __str__(self):
        return str(self.name) + "\n" + str(self.username) + "\n" + str(self.password) + "\n"


class Professor(models.Model):
    name = models.CharField(max_length=40)
    username = models.CharField(max_length=40, unique=True, primary_key=True)
    password = models.CharField(max_length=40)

    def __str__(self):
        return str(self.name) + "\n" + str(self.username) + "\n" + str(self.password) + "\n"


class FacultyAdvisor(models.Model):
    name = models.CharField(max_length=40)
    username = models.CharField(max_length=40, unique=True, primary_key=True)
    password = models.CharField(max_length=40)
    branch = models.CharField(max_length=3)

    def __str__(self):
        return str(self.name) + "\n" + str(self.username) + "\n" + str(self.password) + "\n"


class Student(models.Model):
    roll_number = models.CharField(primary_key=True, max_length=8)
    name = models.CharField(max_length=40)
    branch = models.CharField(max_length=3)
    batch = models.CharField(max_length=1, default='A')
    lab_batch = models.CharField(max_length=2, default='A1')
    tut_batch = models.CharField(max_length=2, default='T1')
    semester = models.IntegerField()
    username = models.CharField(max_length=40, unique=True)
    password = models.CharField(max_length=40)
    image = models.ImageField(upload_to='home/static/images/%Y')

    def __str__(self):
        return str(self.roll_number) + "\n" + str(self.name) + "\n" + str(self.branch) + "\n" + str(self.semester) + "\n" + str(self.username) + "\n" + str(self.password) + "\n" + str(self.image) + "\n"

