
import datetime
from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

#from questions.models import Question



def main_view(request):
    if request.method == 'GET':
        return render(
            request, "main.html",
            context={
                "now": datetime.datetime.now(),
            #    "questions": Question.objects.all()
            }
        )


#@login_required(login_url='/login')
#def q_view(request):
#    return HttpResponse("This is only for authorized users")


def about_view(request):
    if request.method == 'GET':
        return render(
            request,
            "about.html",
            context={
                "now": datetime.datetime.now()
            }
        )

def upload_file(request):
    if request.method == 'POST':
        pass