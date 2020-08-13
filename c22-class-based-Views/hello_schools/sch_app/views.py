# from django.shortcuts import render
from django.views.generic import (
    TemplateView, ListView, DetailView,
    CreateView, UpdateView, DeleteView)

from django.urls import reverse_lazy
from sch_app.models import School, Student


# Simple Template View
class IndexView(TemplateView):
    template_name = 'index.html'


"""
ListView
--------
If you don't mention template_name and context_object_name,
default template_name = 'school_list.html'
default context_object_name = 'school_list'

The school_list comes from adding '_list' after model_name.lower().
Here model name is School.

If can also pass the custom template_name and context_object_name,
template_name = 'sch_app/schools.html'
context_object_name = 'schools'

DetailView
----------
If you don't mention template_name and context_object_name,
template_name = 'sch_app/school_detail.html'
default context_object_name = 'school'
Here model name is School.

If can also pass the custom template_name and context_object_name,
template_name = 'sch_app/the_school_detail.html'
context_object_name = 'school_detail'


CreateView
----------
If you don't mention template_name,
template_name = 'sch_app/school_form.html'

Mandatory component:
Needs get_absolute_url() in the model class where it redirects after creation.


DeleteView
----------
Mandatory component:
1. A template with name = 'school_confirm_delete.html'
2. success_url

The template must be added in the template folder and declaration in the class
is not needed. It takes this delete confirmation template by defaul.

success_url must be declared in the class where it redirects after deletion.
"""


class SchoolListView(ListView):
    model = School


class SchoolDetailView(DetailView):
    model = School


class SchoolCreateView(CreateView):
    model = School

    fields = ('name', 'principal', 'location')


class SchoolUpdateView(UpdateView):
    model = School

    fields = ('name', 'principal')


class SchoolDeleteView(DeleteView):
    model = School

    # Redirects to '/sch_app/school_list' on success.
    # reverse_lazy is used to perform the redirection after successful deletion
    success_url = reverse_lazy('sch_app:school_list')


# Student
class StudentCreateView(CreateView):
    model = Student

    fields = '__all__'
