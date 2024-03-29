from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    list_student = Student.objects.order_by('group').all()
    context = {'object_list': list_student}

    return render(request, template, context)
