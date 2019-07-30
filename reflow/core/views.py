from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from reflow.core.models import Candidate
from reflow.core.forms import CandidateForm


def home(request):
    cand = Candidate.objects.all()

    context = {
        'candidate': cand,
        'new_candidate': form(request),
    }
    return render(request, 'index.html', context)


def form(request):
    if request.method == "POST":
        print(request.POST)
        form = CandidateForm(request.POST or None, request.FILES)
        print(f'form valid: {form}')
        if form.is_valid():
            print('-********' * 20)
            print('entra aqui')
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = CandidateForm()
    return form
