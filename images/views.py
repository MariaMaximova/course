from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.
from .forms import ImageCreateForm
from .models import Image


@login_required
def image_create(request):
    if request.method == 'POST':
        form = ImageCreateForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_item = form.save(commit=False)

            # Добавляем пользователя к созданному объекту.
            new_item.user = request.user
            new_item.save()
            messages.success(request, 'Image added successfully')

            # Перенаправляем пользователя на страницу сохраненного изображения.
            return redirect(new_item.get_absolute_url())
        else:
            # Заполняем форму данными из GET-запроса.
            form = ImageCreateForm(data=request.GET)
            return render(request,
                          'create.html',
                          {'section': 'images', 'form': form})


def image_detail(request, id, slug):
    image = get_object_or_404(Image, id=id, slug=slug)
    return render(request,
                  'detail.html',
                  {'section': 'images', 'image': image})


