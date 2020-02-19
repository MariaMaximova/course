from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect

from .forms import CommentForm
from datetime import datetime, timedelta
from .models import Post


def index(request):
    posts = Post.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(posts, 3)

    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {'posts': paged_listings}
    return render(request, 'posts.html', context)


def article(request, pk):
    post = get_object_or_404(Post, id=pk)
    return render(request, 'post.html', {"post": post})


def search(request):
    return render(request, 'posts.html')
