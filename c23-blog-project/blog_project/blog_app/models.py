from django.db import models
from django.utils import timezone
from django.urls import reverse


class Post(models.Model):
    author = models.ForeignKey('auth.User')  # Superuser
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    publish_date = models.DecimalField(blank=True, null=True)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def approved_comments(self):
        return self.comments.filter(approved=True)

    def get_absolute_url(self):
        return reverse('post_details', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('blog_app.Post', related_name='comments')
    author = models.CharField(max_length=40)  # Anyone
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    approved = models.BooleanField(default=False)

    def approve(self):
        self.approved = True
        self.save()

    def get_absolute_url(self):
        return reverse('post_list')

    def __str__(self):
        return self.text
