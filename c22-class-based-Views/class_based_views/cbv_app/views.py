# from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse


# Create your views here.
class ClassBasedView(View):
    def get(self, request):
        return HttpResponse("Class Based Views are awesome!")
