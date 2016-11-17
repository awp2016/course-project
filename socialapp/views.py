from django.shortcuts import redirect, render

from . import models
from . import forms


def index(request):
    status_list = models.Status.objects.all()

    if request.method == 'GET':
        form = forms.StatusForm()
    elif request.method == 'POST':
        form = forms.StatusForm(request.POST)
        if form.is_valid():
            status = models.Status(text=form.cleaned_data['text'])
            status.save()
            return redirect('index')

    context = {
        'status_list': status_list,
        'form': form,
    }
    return render(request, 'socialapp/index.html', context)


def status_details(request, pk):
    status = models.Status.objects.get(pk=pk)
    context = {'status': status}
    return render(request, 'socialapp/status_details.html', context)
