from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Status(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User)

    def __unicode__(self):
        return '{} by {}'.format(self.text, self.author.get_full_name())

    def get_absolute_url(self):
        return reverse('status_details',
                       kwargs={'pk': self.pk})


class Comment(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User)
    status = models.ForeignKey(Status)


class UserProfile(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    SEX_CHOICES = (
        (MALE, 'M'),
        (FEMALE, 'F'),
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthday = models.DateField(null=True)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, default=MALE)
    avatar = models.ImageField(null=True, upload_to='images')
    user = models.OneToOneField(User, primary_key=True, related_name='profile')
