# from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from . import models


# Simple Template View
class IndexView(TemplateView):
    template_name = 'index.html'


"""
For ListView, if you don't mention template_name and context_object_name,
default template_name = 'school_list.html'
default context_object_name = 'school_list'

The school_list comes from adding '_list' after model name.
Here model name is School.

For DetailView, if you don't mention context_object_name,
default context_object_name = 'school'
Here model name is School.
"""


class SchoolListView(ListView):
    model = models.School

    template_name = 'sch_app/schools.html'
    context_object_name = 'schools'


class SchoolDetailView(DetailView):
    model = models.School

    template_name = 'sch_app/school_detail.html'
    context_object_name = 'school_detail'
