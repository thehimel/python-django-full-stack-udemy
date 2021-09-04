from django.shortcuts import render


def index(request):
    return render(request, "login_app/index.html")


def pages(request):
    return render(request, "login_app/pages.html")


# Used to exercise Template Filters
def users(request):
    user_details = {"username": "johnsmith", "age": 20}
    return render(request, "login_app/users.html", context=user_details)
