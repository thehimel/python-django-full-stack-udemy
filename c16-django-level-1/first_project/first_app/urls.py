from django.conf.urls import url
from first_app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^access_records/', views.access_records, name='access_records'),
    url(r'^contact/', views.contact_form_view, name='contact_form'),
]