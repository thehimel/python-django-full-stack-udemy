# from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import HttpResponse


# Class Based Views

# Simple CLass Based View
class SimpleView(View):
    def get(self, request):
        return HttpResponse("Class Based Views are awesome!")


# Simple Template View
class SimpleTemplateView(TemplateView):
    template_name = 'cbv_app/index.html'


# Template View with Context
class ContextTemplateView(TemplateView):
    template_name = 'cbv_app/view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # context is a dictionary here
        context['message'] = 'This is a Template View with Context.'
        return context
