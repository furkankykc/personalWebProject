from django.utils import timezone
from django.db import models


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField(max_length=9999, blank=True, null=True)
    picture = models.CharField(max_length=30, blank=True, null=True)
    keywords = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
# topic = models.ForeignObject()
#


# class topic (models.Model):
#     name = models.CharField(max_length=50)
