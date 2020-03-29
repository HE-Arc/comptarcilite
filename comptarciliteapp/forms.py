from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class UserCreationFormImproved(UserCreationForm):
    username = forms.CharField(max_length=30,label="Nom d'utilisateur")
    email = forms.EmailField(max_length=200,label="Adresse courriel")
    password1 = forms.CharField(widget = forms.PasswordInput,label="Mot de passe")
    password2 = forms.CharField(widget = forms.PasswordInput,label="Confirmation")


    def clean(self):
       email = self.cleaned_data.get('email')
       if User.objects.filter(email=email).exists():
            raise ValidationError("Adresse courriel déjà utilisée")
       return self.cleaned_data

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )
