from django.conf.urls import url
from cbv_app import views

# from django.urls import path

app_name = "cbv_app"

urlpatterns = [
    url(r"^$", views.SimpleTemplateView.as_view(), name="index"),
    url(r"^simple_view/$", views.SimpleView.as_view(), name="simple_view"),
    url(
        r"^simple_template_view/$",
        views.SimpleTemplateView.as_view(),
        name="simple_template_view",
    ),
    url(
        r"^context_template_view/$",
        views.ContextTemplateView.as_view(),
        name="context_template_view",
    ),
]
