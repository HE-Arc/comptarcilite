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
from .tokens import account_activation_token
from django.contrib.sites.shortcuts import get_current_site

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.core.mail import EmailMessage


## Création de compte utilisateur
class UserAccountCreateView(View):
    def get(self, request):
        context = {}
        form = UserCreationFormImproved()
        return render(request, 'registration/signup.html', {'form': form})

    def post(self, request):
        form = UserCreationFormImproved(request.POST)
        
        print(form.is_valid())
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            email_subject = 'Activate Your Account'
            message = render_to_string('registration/activate_user.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')

            email = EmailMessage(email_subject, message,from_email='no-reply@comptarcilite.tk' ,to=[to_email])
            email.send()

            
            return HttpResponse('We have sent you an email, please confirm your email address to complete registration')

            #username = form.cleaned_data.get('username')
            #raw_password = form.cleaned_data.get('password1')
            #user = authenticate(username=username, password=raw_password)
            #login(request, user)

            #return redirect('index')
        else:
            form = UserCreationFormImproved()

        return render(request, 'registration/signup.html',  {'form': form})

def activate_account(request, uidb64, token):
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return render(request, 'index.html',  {'message': "Votre compte a été vérifié"})
    else:
        return HttpResponse("Lien d'activation invalide")
