from django.shortcuts import render

from . import models


def index(request):
    status_list = models.Status.objects.all()
    return render(request, 'socialapp/index.html',
                  {'status_list': status_list})


def status_details(request, pk):
    status = models.Status.objects.get(pk=pk)
    context = {'status': status}
    return render(request, 'socialapp/status_details.html', context)
