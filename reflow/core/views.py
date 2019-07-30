from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from reflow.core.models import Candidate
from reflow.core.forms import CandidateForm, DeleteForm, EditForm


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def home(request):
    cand = Candidate.objects.all()
    if request.method == 'POST':
        print(request.POST)
        if '_edit' in request.POST:
            edit(request)
        elif '_delete' in request.POST:
            delete(request)

    context = {
        'candidate': cand,
        'new_candidate': form(request),
        # 'edit': edit(request),
        # 'delete': delete(request),
    }
    return render(request, 'index.html', context)


def form(request):
    if request.method == "POST":
        form = CandidateForm(request.POST or None, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = CandidateForm()
    return form


def delete(request):
    if request.method == "POST":
        form = DeleteForm(request.POST or None)
        if form.is_valid():
            Candidate.objects.filter(email=form['email'].value()).delete()
            print('deletando elemento')
            return HttpResponseRedirect(request.path_info)
    else:
        form = CandidateForm()
    return form


def edit(request):
    if request.method == "POST":
        form = EditForm(request.POST or None, request.FILES)
        print(form)
        print(form.is_valid())
        edit = Candidate.objects.filter(email=form['email'].value())
        print(Candidate.objects.filter(email=form['email']))
        if form.is_valid():
            print('editando')
            # post = form.save(commit=False)
            # post.author = request.user
            # post.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = CandidateForm()
    return form
