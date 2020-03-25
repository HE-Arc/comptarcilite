from django.shortcuts import render, redirect
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


class AccountCreateView(View):
    def get(self, request):
        context = {}
        return render(request, 'account_details.html', context)

    def post(self, request):
        result = 'ok'
        try:
            account = Account()
            account.name = request.POST.get("nom_compte")
            account.description = request.POST.get("descr_compte")
            account.save()

            mem = Membership()
            mem.user = request.user
            mem.account = account
            mem.is_owner = True
            mem.save()
        except:
            result = 'error'

        context = {
            'result': result,
            'nom_compte': request.POST.get("nom_compte"),
            'descr_compte': request.POST.get("descr_compte"),
        }
        return render(request, 'account_details.html', context)


class AccountEditView(View):
    def get(self, request, pk):
        account = Account.objects.get(pk=pk)
        context = {'nom_compte': account.name,
                   'descr_compte': account.description,
                   'membres_compte': account.members}
        return render(request, 'account_details.html', context)

    def post(self, request, pk):
        result = 'ok'
        try:
            account = Account.objects.get(pk=pk)
            account.name = request.POST.get("nom_compte")
            account.description = request.POST.get("descr_compte")
            account.save()
        except:
            result = 'error'

        context = {
            'result': result,
            'nom_compte': request.POST.get("nom_compte"),
            'descr_compte': request.POST.get("descr_compte"),
        }
        return render(request, 'account_details.html', context)

class TransactionCreateView(View):
    def post(self, request):
        result = 'ok'
        try:
            trans = Transaction()
            trans.timestamp = request.POST.get('timestamp_trans')
            trans.amount = request.POST.get('amount_trans')
            trans.description = request.POST.get('descr_trans')
            trans.account = Account.objects.get(pk=request.POST.get('id_account_trans'))
            trans.user = request.user
        except:
            result = 'error'

        return redirect('index')


from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import UserCreationFormImproved
#from mysite.core.tokens import account_activation_token

## Création de compte utilisateur
class UserAccountCreateView(View):
    def get(self, request):
        context = {}
        form = UserCreationFormImproved()
        return render(request, 'registration/signup.html', {'form': form})

    def post(self, request):
        form = UserCreationFormImproved(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)

            return redirect('index')
        else:
            form = UserCreationFormImproved()

        return render(request, 'registration/signup.html',  {'form': form})
