
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [

    path('register', views.register),
    path('login', views.login_view),
    path('logout', views.logout_view),
    path('verify-email', views.verify_view),
    path('dashboard', views.dashboard_view),
    path('edit', views.edit),

    # change password urls
    path('password_change/',
         auth_views.PasswordChangeView.as_view()),

    path('password_change/done/',
         auth_views.PasswordChangeDoneView.as_view()),


 #   path('', views.dashboard)

]


