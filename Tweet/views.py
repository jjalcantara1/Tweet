from django.shortcuts import render
from django.views.generic import CreateView


def home(request):
    return render(request, 'home.html', {})


