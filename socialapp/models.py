from __future__ import unicode_literals

from django.db import models


class Status(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    author = models.CharField(default="Eau de Web", max_length=50)

    def __unicode__(self):
        return '{} by {}'.format(self.text, self.author)


class Comment(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    author = models.CharField(default="Eau de Web", max_length=50)
    status = models.ForeignKey(Status)
