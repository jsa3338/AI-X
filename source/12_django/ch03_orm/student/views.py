from django.shortcuts import render
from .models import Student

# Create your views here.

def list(request):
    students = Student.objects.all()
    return render(request, "student/list.html", {"students":students})
