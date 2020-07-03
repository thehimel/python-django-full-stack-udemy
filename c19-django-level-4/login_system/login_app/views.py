from django.shortcuts import render


def index(request):
    return render(request, 'login_app/index.html')


def pages(request):
    return render(request, 'login_app/pages.html')


def users(request):
    return render(request, 'login_app/users.html')
