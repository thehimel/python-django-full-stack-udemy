from django.conf.urls import url
from first_app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^access_records/', views.access_records, name='access_records'),
    url(r'^contact/', views.contact_form_view, name='contact_form'),
    url(r'^registration/', views.registration_form, name='registration_form'),
    url(r'^signup/', views.user_signup_form, name='user_signup_form'),
]