from django.contrib import admin
from .models import Attendance, TimeTable, ProfessorTimeTable as ptt, StudentSubject as ss
from django.contrib.auth.models import Group, User


class AttendView(admin.ModelAdmin):
    list_display = ('date', 'roll_number', 'status', 'lecture')
    list_filter = ('date', 'lecture')
    search_fields = ('date', 'roll_number')


class TTView(admin.ModelAdmin):
    list_display = ('batch', 'time', 'day', 'lecture')
    list_filter = ('time', 'lecture', 'day', 'batch')
    search_fields = ('day', 'time')


class PTTView(admin.ModelAdmin):
    list_display = ('prof_username', 'start_time', 'end_time', 'day', 'class_name', 'lecture')
    list_filter = ('prof_username', 'start_time', 'end_time', 'day')
    search_fields = ('prof_username', 'class_name')


class StudentS(admin.ModelAdmin):
    list_display = ('branch', 'semester', 'lecture')
    list_filter = ('branch', 'semester')
    search_fields = ('branch', 'semester', 'lecture')


admin.site.site_header = 'Smart Attendance System'
admin.site.register(Attendance, AttendView)
admin.site.register(TimeTable, TTView)
admin.site.register(ptt, PTTView)
admin.site.register(ss, StudentS)
admin.site.unregister(Group)
admin.site.unregister(User)
