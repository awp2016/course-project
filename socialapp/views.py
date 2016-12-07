from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render

from . import models
from . import forms


@login_required
def index(request):
    status_list = models.Status.objects.order_by('-date_added')
    if request.method == 'GET':
        form = forms.StatusForm()
    elif request.method == 'POST':
        form = forms.StatusForm(request.POST)
        if form.is_valid():
            status = models.Status(text=form.cleaned_data['text'],
                                   author=request.user)
            status.save()
            return redirect('index')

    context = {
        'status_list': status_list,
        'form': form,
    }
    return render(request, 'socialapp/index.html', context)


@login_required
def status_details(request, pk):
    status = models.Status.objects.get(pk=pk)
    comments = (
        models.Comment.objects
        .filter(status=status)
        .order_by('-date_added')
    )
    if request.method == 'GET':
        form = forms.CommentForm()
    elif request.method == 'POST':
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            comment = models.Comment(text=form.cleaned_data['text'],
                                     status=status,
                                     author=request.user)
            comment.save()
            return redirect('status_details', pk=status.pk)

    context = {
        'status': status,
        'form': form,
        'comments': comments
    }
    return render(request, 'socialapp/status_details.html', context)


def login_view(request):
    if request.method == 'GET':
        form = forms.LoginForm()
    elif request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user:
                login(request=request,
                      user=user)
                return redirect('index')
    context = {
        'form': form
    }
    return render(request, 'socialapp/login.html', context)


def logout_view(request):
    if request.method == 'GET':
        logout(request)
        return redirect('login')


def user_profile(request, pk):
    if request.method == 'GET':
        user_profile = models.UserProfile.objects.get(pk=pk)
    context = {
        'user_profile': user_profile,
    }
    return render(request, 'socialapp/user_profile.html', context)
