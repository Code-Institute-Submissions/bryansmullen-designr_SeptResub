from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import BlogEntry


@login_required(login_url='/users/login')
def blog_entry_list(request):
    blog_entries = BlogEntry.objects.all()
    context = {
        'blog_entries': blog_entries
    }
    return render(request, 'blog/blog-list.html', context)
