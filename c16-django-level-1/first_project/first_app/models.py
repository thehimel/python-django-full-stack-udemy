from django.db import models

# Create your models here.

class Topic(models.Model):
    topic_name = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return self.topic_name

class Webpage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=256, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)

"""
python manage.py migrate
python manage.py makemigrations first_app
python manage.py migrate

python manage.py shell
from first_app.models import Topic
t = Topic(topic_name="Social Network")
t.save()
print(Topic.objects.all())
print(t)
"""
