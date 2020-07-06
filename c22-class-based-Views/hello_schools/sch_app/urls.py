from django.urls import path
from . import views

app_name = 'sch_app'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('schools/', views.SchoolListView.as_view(), name='schools'),

    # Example url = /sch_app/school_detail/1
    # Here slug_field, pk = 1
    # We must use slug_field = 'pk' for the generic DetailView
    path(
        'school_detail/<int:pk>',
        views.SchoolDetailView.as_view(), name='school_detail'),
]
