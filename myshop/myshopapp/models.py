from django.db import models
from django.utils import timezone

# Create your models here.
class Product(models.Model):
    image = models.ImageField(upload_to='uploads/product/')
    title = models.CharField(default='', max_length=255, blank=False)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title