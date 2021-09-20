from django.contrib import admin

from .models import BlogEntry


class BlogEntryAdmin(admin.ModelAdmin):
    """
    This class defines how blog entries will be displayed in the admin backend
    """
    readonly_fields = ('id',)
    fields = ('title', 'content', 'author', 'date_entered')
    list_display = ('id', 'title', 'author', 'date_entered')
    ordering = ('-date_entered',)


admin.site.register(BlogEntry, BlogEntryAdmin)
