from django.db import models


class PortfolioEntry(models.Model):
    """
    This class defines the PortfolioEntry model
    """
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='portfolio/%Y/%m/%d/')

    def __str__(self):
        return self.title
