from django.shortcuts import render
from reflow.core.models import *


def home(request):
    return render(request, 'index.html')
