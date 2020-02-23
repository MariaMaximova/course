
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse


# def main_view(request):
#    if request.method == 'GET':
#        return render(request, 'main.html')


def about_view(request):
    if request.method == 'GET':
        return render(request, "about.html")


def main_view(request):
    if request.method == 'GET':
        return render(request, "main.html")