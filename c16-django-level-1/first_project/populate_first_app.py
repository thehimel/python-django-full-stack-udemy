import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

# Fake Population Script
import random
from faker import Faker
from first_app.models import Topic, Webpage, AccessRecord

fakegen = Faker()
topics = ['Search Engine', 'Social Network', 'Marketplace', 'News', 'Games']


def add_topic():
    random_topic = random.choice(topics)
    # [0] here is for get_or_create() which returns a tuple.
    the_topic = Topic.objects.get_or_create(topic_name=random_topic)[0]
    return the_topic


def add_webpage():
    # Get or create a topic
    topic = add_topic()

    # Create fake data
    name = fakegen.company()
    url = fakegen.url()
    the_webpage = Webpage.objects.get_or_create(topic=topic, name=name, url=url)[0]

    return the_webpage


def populate(n=5):
    for entry in range(n):
        webpage = add_webpage()  # Get or create a webpage
        date = fakegen.date()  # Fake date
        acc_rec = AccessRecord.objects.get_or_create(name=webpage, date=date)[0]


if __name__ == '__main__':
    print("Populating script started.")
    populate()
    print("Populating complete.")
