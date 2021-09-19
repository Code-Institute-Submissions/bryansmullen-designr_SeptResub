from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from .models import BlogEntry
from .forms import BlogEntryForm
from datetime import datetime


def blog_entry_list(request):
    blog_entries = BlogEntry.objects.all()
    for blog in blog_entries:
        if len(blog.content) > 500:
            blog.content = f'{blog.content[:500]}...'
    context = {
        'blog_entries': blog_entries
    }
    return render(request, 'blog/blog-list.html', context)


@login_required(login_url='/accounts/login/')
def blog_detail(request, blog_id):

    blog_entry = BlogEntry.objects.get(id=blog_id)
    context = {
        'blog_entry': blog_entry
    }
    return render(request, 'blog/blog-detail.html', context)


@login_required(login_url='/accounts/login/')
def blog_new(request):
    if request.method == 'POST':
        # Handle POST request
        new_blog_entry = BlogEntry(
            title=request.POST['title'], content=request.POST['content'],
            author=request.user, date_entered=datetime.now())
        new_blog_entry.save()
        return redirect(reverse('blog_entry_list'))
    else:
        # Handle GET Requeste
        blog_entry_form = BlogEntryForm()

        context = {
            'blog_entry_form': blog_entry_form,
            'function': 'add'
        }
        return render(request, 'blog/blog-add-edit.html', context)


@login_required(login_url='/accounts/login/')
def blog_edit(request, blog_id):
    if request.method == 'POST':
        # Handle POST request
        existing_entry = BlogEntry.objects.get(id=blog_id)
        existing_entry.title = request.POST['title']
        existing_entry.content = request.POST['content']
        existing_entry.save()
        return redirect(reverse('blog_entry_list'))
    else:
        # Handle GET Request
        current_blog_data = BlogEntry.objects.get(id=blog_id)

        blog_entry_form = BlogEntryForm(instance=current_blog_data)

        context = {
            'blog_entry_form': blog_entry_form,
            'function': 'edit',
            'blog_id': blog_id
        }
        return render(request, 'blog/blog-add-edit.html', context)


@login_required(login_url='/accounts/login/')
def blog_delete(request, blog_id):
    if request.method == 'POST':
        # Handle POST request
        blog_entry = BlogEntry.objects.get(id=blog_id)
        blog_entry.delete()

        return redirect(reverse('blog_entry_list'))
    else:
        # Handle GET Request
        blog_entry = BlogEntry.objects.get(id=blog_id)
        context = {
            'blog_entry': blog_entry
        }
        return render(request, 'blog/blog-delete.html', context)
