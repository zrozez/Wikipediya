from django.db import models
from django.shortcuts import reverse
from categories.models import Category

class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                             null=True, related_name='posts')
    title = models.CharField(max_length=128)
    body = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'id': self.id})
