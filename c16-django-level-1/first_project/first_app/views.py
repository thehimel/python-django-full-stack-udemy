from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord


def index(request):
    my_dictionary = {
        "subject":  "Trees in the Forest.",
    }

    return render(request, 'first_app/index.html', context=my_dictionary)


def access_records(request):
    access_records_list = AccessRecord.objects.order_by('date')

    access_records_dictionary = {
        'access_records': access_records_list
    }

    return render(request, 'first_app/access_records.html', context=access_records_dictionary)
