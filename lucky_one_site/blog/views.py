from django.shortcuts import render
from django.utils import timezone
from .models import Post


def post_list(request):
    posts = Post.objects.filter(pablished_date_lte=timezone.now()).oder_by('pablished_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
