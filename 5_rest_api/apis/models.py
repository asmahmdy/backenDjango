from django.db import models

# Create your models here.

class School(models.Model):
    school_name = models.CharField(max_length=100,null=True)
    school_Abbreviate_name = models.CharField(max_length=100,null=True)
    school_address = models.CharField(max_length=300,null=True)

    def __str__(self):
        return str(self.school_name)
    
class Classroom(models.Model):
    classroom_class = models.CharField(max_length=100,null=True)
    classroom_no = models.CharField(max_length=100,null=True)
    classroom_school = models.ForeignKey(School, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return str(self.classroom_class)
    
class Teacher(models.Model):
    teacher_name = models.CharField(max_length=100, null=True)
    teacher_lastname = models.CharField(max_length=100, null=True)
    teacher_gender = models.CharField(max_length=100, null=True)
    classrooms = models.ManyToManyField(Classroom, related_name='teachers',blank=True)
    teacher_school = models.ForeignKey(School, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f"{self.teacher_name} {self.teacher_lastname}"
    
class Student(models.Model):
    student_name = models.CharField(max_length=100,null=True)
    student_lastname = models.CharField(max_length=100,null=True)
    student_gender = models.CharField(max_length=100,null=True)
    student_classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='students')
    student_school = models.ForeignKey(School, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f"{self.student_name} {self.student_lastname}"