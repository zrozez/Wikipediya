from django.db import models
from django.shortcuts import reverse

class Category(models.Model):

    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category_detail_url', kwargs={'id': self.id})

