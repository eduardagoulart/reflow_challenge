from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from reflow.core.models import Candidate
from reflow.core.forms import CandidateForm, DeleteForm


def home(request):
    cand = Candidate.objects.all()

    context = {
        'candidate': cand,
        'new_candidate': form(request),
        'delete': delete(request),
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
            return HttpResponseRedirect(request.path_info)
    else:
        form = CandidateForm()
    return form
