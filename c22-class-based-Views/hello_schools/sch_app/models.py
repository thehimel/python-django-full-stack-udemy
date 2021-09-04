from django.db import models
from django.urls import reverse


class School(models.Model):
    name = models.CharField(max_length=128)
    principal = models.CharField(max_length=48)
    location = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    # After creating a new school with CreateView,
    # app goes to sch_app/school_detail/<int:pk>
    # pk stands for Primary Key, every object has a unique primary key.
    def get_absolute_url(self):
        return reverse("sch_app:school_detail", kwargs={"pk": self.pk})


class Student(models.Model):
    school = models.ForeignKey(
        School, on_delete=models.CASCADE, related_name="students"
    )

    name = models.CharField(max_length=48)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    # After creating a new student with CreateView,
    # app goes to sch_app/school_detail/<int:pk>
    # Here pk = self.school.pk
    def get_absolute_url(self):
        return reverse("sch_app:school_detail", kwargs={"pk": self.school.pk})
