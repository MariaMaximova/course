from django.urls import path

from . import views

urlpatterns = [
    path('', views.main_view),
    path('about', views.about_view),
    path('main', views.main_view),
#    path('dashboard.html', views.dashboard_view),
  #  path('checkout', views.checkout),
  #  path('contacts', views.contacts)
]