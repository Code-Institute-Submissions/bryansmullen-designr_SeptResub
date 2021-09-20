from django import forms

from .models import BlogEntry


class BlogEntryForm(forms.ModelForm):
    """
    This class defines the form used for blog entries
    """
    class Meta:
        model = BlogEntry
        fields = (
            'title', 'content',
            )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'title': 'Blog Title',
            'content': 'Blog Content',
        }

        self.fields['title'].widget.attrs['autofocus'] = True
        self.fields['content'].widget.attrs['class'] = "materialize-textarea"

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
