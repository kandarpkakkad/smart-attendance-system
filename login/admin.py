from django.contrib import admin
from .models import Professor, Student, Admin, FacultyAdvisor

# Register your models here.


class Stud(admin.ModelAdmin):
    list_display = ('roll_number', 'name', 'username', 'branch', 'batch', 'lab_batch', 'tut_batch', 'semester', 'image')
    list_filter = ('batch', 'lab_batch', 'tut_batch', 'semester', 'branch')
    search_fields = ('roll_number', 'name', 'branch', 'semester', 'batch', 'lab_batch', 'tut_batch', 'username')


class Prof(admin.ModelAdmin):
    list_display = ('name', 'username')
    search_fields = ('name', 'username')


class Adm(admin.ModelAdmin):
    list_display = ('name', 'username')
    search_fields = ('name', 'username')


class FA(admin.ModelAdmin):
    list_display = ('name', 'username', 'branch')
    search_fields = ('name', 'username', 'branch')


admin.site.site_header = 'Smart Attendance System'
admin.site.register(Admin, Adm)
admin.site.register(Professor, Prof)
admin.site.register(Student, Stud)
admin.site.register(FacultyAdvisor, FA)
