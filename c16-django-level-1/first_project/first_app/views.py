from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    my_dictionary = {
        "subject":  "Trees in the Forest.",
    }

    return render(request, 'first_app/index.html', context=my_dictionary)
