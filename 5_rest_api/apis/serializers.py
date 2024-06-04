from rest_framework import serializers
from .models import *

# code here

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'


class SchoolDetailSerializer(serializers.ModelSerializer):
    classroom_count = serializers.IntegerField(source='classrooms.count', read_only=True)
    teacher_count = serializers.SerializerMethodField()
    student_count = serializers.SerializerMethodField()

    class Meta:
        model = School
        fields = ['id', 'name', 'classroom_count', 'teacher_count', 'student_count']

    def get_teacher_count(self, obj):
        return Teacher.objects.filter(classrooms__school=obj).distinct().count()

    def get_student_count(self, obj):
        return Student.objects.filter(classroom__school=obj).count()