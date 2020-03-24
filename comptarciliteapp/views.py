from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic, View
from django.urls import reverse_lazy
from .models import Account, Membership, Transaction, User
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/auth/login")
def index(request):
    context = {}
    return render(request, 'index.html', context)

# def create_account(request):
#     context = {}
#     return render(request, 'create_account.html', context)

class AccountCreateView(View):
    def get(self, request):
        context = {}
        return render(request, 'create_account.html', context)

    def post(self, request):
        account = Account()
        account.name = request.POST.get("nom_compte")
        account.description = request.POST.get("descr_compte")

        account.save()

        mem = Membership()
        mem.user = request.user
        mem.account = account
        mem.is_owner = True

        mem.save()

        return 0
