from django.shortcuts import render

from . import models


def index(request):
    status_list = models.Status.objects.all()
    return render(request, 'socialapp/index.html',
                  {'status_list': status_list})
