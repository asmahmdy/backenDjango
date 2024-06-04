from django import forms
from django.http import JsonResponse
from django.http.response import HttpResponse
from django.urls import reverse_lazy
from .models import *
from .serializers import*
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Count
from django.views.generic.edit import UpdateView



def success(request):
    return render(request, 'success.html')



def school_list(request):
    query = request.GET.get('name')  
    if query:
        schools = School.objects.filter(school_name__icontains=query) 
    else:
        schools = School.objects.all()
    school_count = schools.count()
    return render(request, 'schools/school_list.html', {'schools': schools})

def school_detail(request, school_id):
    school = get_object_or_404(School, pk=school_id)
    classroom_count = school.classroom_set.count()
    teacher_count = school.teacher_set.count()
    student_count = school.student_set.count()
    context = {
        'school': school,
        'classroom_count': classroom_count,
        'teacher_count': teacher_count,
        'student_count': student_count,
    }
    return render(request, 'school_detail.html', context)



class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ['school_name', 'school_Abbreviate_name', 'school_address']

def add_school(request):
    if request.method == 'POST':
        form = SchoolForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success') 
    else:
        form = SchoolForm()
    return render(request, 'schools/add_school.html', {'form': form})


def school_delete(request, school_id):
   
    school = get_object_or_404(School, pk=school_id)
    school.delete()

    return redirect('school_list') 


class SchoolUpdateView(UpdateView):
    model = School
    form_class = SchoolForm
    template_name = 'schools/school_update.html'
    success_url = reverse_lazy('school_list')

def school_update_view(request, pk):
    school = get_object_or_404(School, pk=pk)
    if request.method == 'POST':
        form = SchoolForm(request.POST, instance=school)
        if form.is_valid():
            form.save()
            return HttpResponse("School updated successfully")
    else:
        form = SchoolForm(instance=school)
    
    return render(request, 'schools/school_update.html', {'form': form, 'school': school})


def school_detail(request, school_id):
    # ดึงข้อมูลของโรงเรียน
    school = get_object_or_404(School, pk=school_id)

    # นับจำนวนห้องเรียน
    classroom_count = Classroom.objects.filter(school=school).count()

    # นับจำนวนครู
    teacher_count = Teacher.objects.filter(school=school).count()

    # นับจำนวนนักเรียน
    student_count = Student.objects.filter(school=school).count()

    return render(request, 'school_detail.html', {
        'school': school,
        'classroom_count': classroom_count,
        'teacher_count': teacher_count,
        'student_count': student_count,
    })
