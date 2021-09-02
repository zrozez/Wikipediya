from django.contrib import admin
from comments.models import Comment


class CommentAdmin(admin.ModelAdmin):
    fields = ['post', 'name', 'email', 'body', ]


admin.site.register(Comment, CommentAdmin)


