from django.db import models


class School(models.Model):
    name = models.CharField(max_length=128)
    principal = models.CharField(max_length=48)
    location = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Student(models.Model):
    school = models.ForeignKey(
        School, on_delete=models.CASCADE, related_name='students')

    name = models.CharField(max_length=48)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.name
