from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.decorators.http import require_GET

from .forms import RegistrationForm, ProfileEditForm, UserEditForm
from .models import Profile


def register(request):
    if request.method == 'GET':
        form = RegistrationForm()
        return render(request, 'register.html', context={
            "form": form
        })
    elif request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(user)
            login(request, user)
            """
#            link = user.get_verification_link()
#            user.email_user(
#                "Email confirmation",
#                f"Please follow the <a href='{link}'>link</a>",
#                from_email='admin@adm.com'
#           )
#            user.verification_email_sent_at = timezone.now()
            # Сохраняем пользователя в базе данных."""

            # Создание профиля пользователя.
            Profile.objects.create(user=user)
            user.save()
            return redirect("/")
        else:
            return render(request, 'register.html', context={
                "form": form
            })


def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html', context={
            "error": False
        })
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', context={
                "error": True
            })


@login_required
@require_GET
def verify_view(request):
    print(request.GET.get('key'))
    secret_ket = request.GET.get('key')
    if request.user.check_key(secret_ket):
        return render(request, 'confirmation_success.html')
    else:
        return redirect('dashboard.html')


def logout_view(request):
    logout(request)
    return redirect("/")


def dashboard_view(request):
    return render(request, "dashboard.html")


def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
                                       data=request.POST,
                                       files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        return render(request, 'edit.html',
                      {'user_form': user_form, 'profile_form': profile_form})


