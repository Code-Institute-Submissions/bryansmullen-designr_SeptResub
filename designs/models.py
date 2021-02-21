from datetime import datetime

from django.db import models

class Design(models.Model):
    name = models.CharField(max_length=50)
    # owner = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=50)
    date = models.DateField(default=datetime.now)
    complete = models.BooleanField()
    brief = models.TextField()
    image = models.ImageField(upload_to='designs/%Y/%m/%d/')
    edits_remaining = models.IntegerField(default=2)

    def __str__(self):
        return self.name
