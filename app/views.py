from django.shortcuts import render
from .forms import StudentForm, CourseForm
from .models import Student, Course
from django.http import HttpResponseRedirect

# Create your views here.


def index(request):
    return render(request, 'index.html')


def create_student(request):
    if request.method == "GET":
        return render(request, 'create.html', context={'form': StudentForm()})
    else:
        student = Student()
        student.name = request.POST.get('name')
        course_ids = request.POST.getlist('courses')
        student.save()
        courses = Course.objects.filter(id__in=course_ids)
        student.courses.set(courses)
        return HttpResponseRedirect('/')


def create_course(request):
    if request.method == "GET":
        return render(request, 'create.html', context={'form': CourseForm()})
    else:
        cf = CourseForm(request.POST)
        if cf.is_valid():
            print(**cf.cleaned_data)
            Course.objects.create(**cf.cleaned_data)
        return HttpResponseRedirect('/')
