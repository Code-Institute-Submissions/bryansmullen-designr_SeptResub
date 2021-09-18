from django.shortcuts import render, redirect,reverse
from django.contrib.auth.decorators import login_required

from .models import BlogEntry
from .forms import BlogEntryForm
from datetime import datetime

@login_required(login_url='/users/login')
def blog_entry_list(request):
    blog_entries = BlogEntry.objects.all()
    for blog in blog_entries:
        if len(blog.content) > 50:
            blog.content = f'{blog.content[:50]}...'
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
    return render(request, 'blog/blog-detail.html', context)


@login_required(login_url='/users/login/<blog_id>')
def blog_new(request):
    if request.method == 'POST':
        # Handle POST request
        new_blog_entry = BlogEntry(title=request.POST['title'], content=request.POST['content'], author=request.user, date_entered=datetime.now())
        new_blog_entry.save()
        return redirect(reverse('blog_entry_list'))
    else:
        # Handle GET Requeste
        blog_entry_form = BlogEntryForm()

        context = {
            'blog_entry_form': blog_entry_form
        }
        return render(request, 'blog/blog-new.html', context)
