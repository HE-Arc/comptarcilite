from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic, View
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="/auth/login")
def index(request):
    context = {}
    return render(request, 'index.html', context)


def create_account(request):
    context = {}
    return render(request, 'create_account.html', context)
