from django.shortcuts import render, redirect
from reflow.core.models import Candidate
from reflow.core.forms import CandidateForm


def home(request):
    cand = Candidate.objects.all()

    '''if request.method == "POST":
        print(request.POST)
        form = CandidateForm(request.POST)
        print(f'form valid: {form}')
        if form.is_valid():
            print('entra aqui')
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('index', pk=post.pk)
    else:
        print('estou caindo num else')
        form = CandidateForm()'''

    context = {
        'candidate': cand,
        # 'new_candidate': form,
    }
    return render(request, 'index.html', context)


def new(request):
    if request.method == "POST":
        print(request.POST)
        form = CandidateForm(request.POST)
        print(f'form valid: {form}')
        if form.is_valid():
            print('entra aqui')
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('index', pk=post.pk)
    else:
        print('estou caindo num else')
        form = CandidateForm()
    return render(request, 'new.html', {'form': form})
