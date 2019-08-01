from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from reflow.core.models import Candidate
from reflow.core.forms import CandidateForm, DeleteForm, EditForm


def success(request):
    return render(request, 'success.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def user_details(request):
    return render(request, 'user.html', {'form': add_user(request)})


def add_user(request):
    if request.method == "POST":
        form = CandidateForm(request.POST or None, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('success')
    else:
        form = CandidateForm()
    return form


@login_required()
def home(request):
    cand = Candidate.objects.all()
    print(f'home {cand}')
    if request.user.is_authenticated:
        context = {
            'candidate': cand,
            'new_candidate': add(request),
        }
        return render(request, 'index.html', context)

    else:
        form = UserCreationForm()
        return render(request, 'access_denied.html', {'form': form})


def see_everything(request, email):
    cand = Candidate.objects.filter(email=email).values()
    return render(request, 'see_all.html', {'candidate': cand})


def add(request):
    if request.method == "POST":
        form = CandidateForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = CandidateForm()
    return form


def delete(request, email):
    print(email)
    print(request.method)

    return redirect('home')
    '''if request.method == "POST":
        form = DeleteForm(request.POST or None)
        if form.is_valid():
            Candidate.objects.filter(email=form['email'].value()).delete()
            print('deletando elemento')
            return HttpResponseRedirect(request.path_info)
    else:
        form = CandidateForm()
    return form'''


def edit(request, email):
    if request.method == "POST":
        form = EditForm(request.POST)

        if form.is_valid():
            Candidate.objects.filter(email=email).update(name=form['name'].value())
            Candidate.objects.filter(email=email).update(skills=form['skills'].value())
            Candidate.objects.filter(email=email).update(phone_number=form['phone_number'].value())
            Candidate.objects.filter(email=email).update(github=form['github'].value())
            Candidate.objects.filter(email=email).update(portifolio=form['portifolio'].value())
            Candidate.objects.filter(email=email).update(experiencia=form['experiencia'].value())
            return redirect('home')
    else:
        form = EditForm()
    return render(request, 'edit.html', {'form': form})
