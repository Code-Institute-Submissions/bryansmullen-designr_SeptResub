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


@login_required(login_url='/users/login/<blog_id>')
def blog_detail(request,blog_id):
    blog_entry = BlogEntry.objects.get(id=blog_id)
    context = {
        'blog_entry': blog_entry
    }

    print(blog_id)
    return render(request, 'blog/blog-detail.html', context)
