from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    #path('login/',TemplateView.as_view(template_name="registration/login.html"),name='login'),
    path('admin/', admin.site.urls),
    path('auth/login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('create_account/', views.AccountCreateView.as_view(), name='create_account'),
    path('edit_account/<pk>', views.AccountEditView.as_view(), name='edit_account'),
    path('users/', views.get_user_list, name='users_list_api'),

    path('auth/', auth_views.LoginView.as_view(redirect_authenticated_user=True)),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('auth/password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('auth/password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('auth/password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset'),
    path('auth/password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('auth/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('auth/reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('auth/signup/',views.UserAccountCreateView.as_view(),name='signup'),

    path('auth/activate/<uidb64>/<token>/',views.activateAccountUser, name='activate'),
    
    path('', views.index, name='index'),
    path('listAccounts/', views.listAccounts, name='listAccounts'),
]
