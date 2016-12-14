from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView

from . import models
from . import forms


class StatusListView(LoginRequiredMixin, ListView):
    model = models.Status
    form_class = forms.StatusForm
    template_name = 'socialapp/index.html'

    def get_context_data(self, **kwargs):
        context = super(StatusListView, self).get_context_data(**kwargs)
        context['form'] = self.form_class()
        return context

    def get_queryset(self):
        return self.model.objects.order_by('-date_added')

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            status = self.model(text=form.cleaned_data['text'],
                                author=request.user)
            status.save()
            return redirect('index')


class StatusUpdate(LoginRequiredMixin, UpdateView):
    model = models.Status
    fields = ['text']
    template_name = 'socialapp/update_status.html'


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


def edit_user_profile(request, pk):
    user_profile = models.UserProfile.objects.get(pk=pk)
    form = forms.ProfileForm(initial={
        'first_name': user_profile.first_name,
        'last_name': user_profile.last_name
    })
    if request.method == 'POST':
        form = forms.ProfileForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            user_profile.first_name = first_name
            user_profile.last_name = last_name
            user_profile.save()
            return redirect('user_profile', pk=pk)

    context = {
        'user_profile': user_profile,
        'form': form,
    }
    return render(request, 'socialapp/edit_profile.html', context)
