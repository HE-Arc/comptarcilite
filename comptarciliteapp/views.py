from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic, View
from django.urls import reverse_lazy


# Create your views here.
def index(request):
    context = {}
    return render(request, 'index.html', context)


def create_account(request):
    context = {}
    return render(request, 'create_account.html', context)


