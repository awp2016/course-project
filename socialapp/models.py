from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Status(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User)

    def __unicode__(self):
        return '{} by {}'.format(self.text, self.author.get_full_name())


class Comment(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User)
    status = models.ForeignKey(Status)
