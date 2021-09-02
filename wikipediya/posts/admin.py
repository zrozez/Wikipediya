from django.contrib import admin
from posts.models import Post

class PostAdmin(admin.ModelAdmin):
    field = ['category', 'title', 'body', ]

admin.site.register(Post, PostAdmin)
