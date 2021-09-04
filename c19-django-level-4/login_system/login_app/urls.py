from django.conf.urls import url, include
from login_app import views

app_name = "login_app"

urlpatterns = [
    url(r"^$", views.index, name="index"),
    url(r"^pages", views.pages, name="pages"),
    url(r"^users", views.users, name="users"),
]
