from django.contrib import admin
from .models import *
# Register your models here.

class SchoolAdmin(admin.ModelAdmin):
    list_display = ('id','school_name','school_Abbreviate_name','school_address')
admin.site.register(School, SchoolAdmin)

class ClassroomAdmin(admin.ModelAdmin):
    list_display = ('classroom_school','classroom_class','classroom_no')
admin.site.register(Classroom, ClassroomAdmin)

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('teacher_name', 'teacher_lastname', 'teacher_gender', 'teacher_school','get_classrooms')
        
    def get_classrooms(self, obj):
        return ", ".join([classroom.name for classroom in obj.classrooms.all()])
    get_classrooms.short_description = 'Classrooms'

admin.site.register(Teacher, TeacherAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'student_lastname', 'student_gender', 'student_school','student_classroom')

admin.site.register(Student, StudentAdmin)