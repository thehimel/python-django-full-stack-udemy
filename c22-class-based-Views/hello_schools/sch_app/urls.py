from django.urls import path
from . import views

app_name = 'sch_app'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('school_list/', views.SchoolListView.as_view(), name='school_list'),

    # Example url = /sch_app/school_detail/1
    # Here slug_field, pk = 1
    # We must use slug_field = 'pk' for the generic DetailView
    path(
        'school_detail/<int:pk>',
        views.SchoolDetailView.as_view(), name='school_detail'),

    path('create/', views.SchoolCreateView.as_view(), name='create'),
    path('update/<int:pk>', views.SchoolUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.SchoolDeleteView.as_view(), name='delete'),

    # Student
    path(
        'create_student/',
        views.StudentCreateView.as_view(), name='create_student'),
]
