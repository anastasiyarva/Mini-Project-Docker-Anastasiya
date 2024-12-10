from django.contrib import admin
from .models import Timetable, Course, Student
from django.contrib.admin import AdminSite


class MyAdminSite(AdminSite):
    site_header = "Welcome Anastasiya!"  
    site_title = "Welcome Anastasiya!"  
    index_title = "Welcome to the Anastasiya Portal!"
    
admin_site = MyAdminSite(name='myadmin')

class TimetableAdmin(admin.ModelAdmin):
    list_display = ('course', 'student', 'level', 'room', 'time', 'day')
    list_display_links = ('course',)
    list_filter = ('level',)




admin.site.register(Timetable, TimetableAdmin)
admin.site.register(Course)
admin.site.register(Student)