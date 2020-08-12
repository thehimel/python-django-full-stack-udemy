from django.db import models


# Models: Topic Webapge AccessRecord
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


# Model: UserDetails
class UserDetails(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField(max_length=64, unique=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


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
