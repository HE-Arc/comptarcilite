from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    #path('login/',TemplateView.as_view(template_name="registration/login.html"),name='login'),
    #path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
    path('auth/login', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('create_account', views.AccountCreateView.as_view(), name='create_account'),
    path('', views.index, name='index'),
]
