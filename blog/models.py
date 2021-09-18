from django.db import models
from django.contrib.auth.models import User


class BlogEntry(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='blog_entry'
        )
    date_entered = models.DateField()

    def __str__(self):
        return self.title
