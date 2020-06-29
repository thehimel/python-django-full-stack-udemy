from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    my_dictionary = {
        "insert_me":  "I am coming from first_app/views.py",
    }

    return render(request, 'first_app/index.html', context=my_dictionary)
