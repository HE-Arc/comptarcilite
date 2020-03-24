from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('auth/', auth_views.LoginView.as_view(redirect_authenticated_user=True)),
    path('auth/login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
    #path('create_account', views.create_account, name='create_account'),
    path('', views.index, name='index'),
]
