from django.db import models


class Service(models.Model):
    """
    This class defines the Service model
    """
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='services/%Y/%m/%d/')

    def __str__(self):
        return self.name
