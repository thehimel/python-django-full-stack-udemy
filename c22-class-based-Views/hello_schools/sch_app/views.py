# from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from sch_app.models import School


# Simple Template View
class IndexView(TemplateView):
    template_name = 'index.html'


"""
ListView
--------
For ListView, if you don't mention template_name and context_object_name,
default template_name = 'school_list.html'
default context_object_name = 'school_list'

The school_list comes from adding '_list' after model_name.lower().
Here model name is School.

If can also pass the custom template_name and context_object_name,
template_name = 'sch_app/schools.html'
context_object_name = 'schools'

DetailView
----------
For DetailView, if you don't mention context_object_name,
template_name = 'sch_app/school_detail.html'
default context_object_name = 'school'
Here model name is School.

If can also pass the custom template_name and context_object_name,
template_name = 'sch_app/the_school_detail.html'
context_object_name = 'school_detail'
"""


class SchoolListView(ListView):
    model = School


class SchoolDetailView(DetailView):
    model = School
