from django.shortcuts import render, get_object_or_404
from posts.models import Post
from comments.models import Comment
from comments.forms import CommentForm


def post_detail_view(request, id):
    post = get_object_or_404(Post, id=id)
    comments = post.comments.filter(active=True)
    comment_form = CommentForm()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    return render(request, 'posts/post_detail.html', context={'post': post,
                                                             'comments': comments,
                                                             'comment_form': comment_form,
    })