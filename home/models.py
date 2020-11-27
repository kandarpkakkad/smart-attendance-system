from django.db import models

# Create your models here.
"""
    1. Attendance
    2. Time Table
    3. Professor Time Table
    4. Student Subjects
"""


class Attendance(models.Model):
    date = models.DateField(auto_now_add=True)
    roll_number = models.CharField(max_length=8)
    status = models.CharField(max_length=1)
    prof_username = models.CharField(max_length=40)
    lecture = models.CharField(max_length=40)
    lecture_type = models.CharField(max_length=2, default='0')
    
    def __str__(self):
        return str(self.date) + "\n" + str(self.roll_number) + "\n" + str(self.status) + "\n" + str(self.prof_username) + "\n" + str(self.lecture) + "\n"


class TimeTable(models.Model):
    batch = models.CharField(max_length=4)
    time = models.TimeField()
    day = models.CharField(max_length=10, default='sunday')
    lecture = models.CharField(max_length=10)

    def __str__(self):
        return str(self.batch) + "\n" + str(self.time) + "\n" + str(self.day) + "\n" + str(self.lecture) + "\n"


class ProfessorTimeTable(models.Model):
    prof_username = models.CharField(max_length=40)
    start_time = models.TimeField(default='09:00:00')
    end_time = models.TimeField(default='18:05:00')
    day = models.CharField(max_length=10, default='sunday')
    class_name = models.CharField(max_length=10)
    lecture = models.CharField(max_length=10)

    def __str__(self):
        return str(self.prof_username) + "\n" + str(self.start_time) + "\n" + str(self.end_time) + "\n" + str(self.day) + "\n" + str(self.lecture) + "\n" + str(self.class_name) + "\n"


class StudentSubject(models.Model):
    branch = models.CharField(max_length=10)
    semester = models.IntegerField()
    lecture = models.CharField(max_length=40)
    lecture_type = models.CharField(max_length=2)

    def __str__(self):
        return str(self.branch) + "\n" + str(self.semester) + "\n" + str(self.lecture) + "\n" + str(self.lecture_type) + "\n"
