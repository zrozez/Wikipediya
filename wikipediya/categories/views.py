from django.shortcuts import get_object_or_404, render
from categories.models import Category
from posts.models import Post

def categories_list_view(request):
    categories = Category.objects.all()
    return render(request, 'categories/index.html', context={'categories':categories, })


def category_detail_view(request, id):
    category = get_object_or_404(Category, id=id)
    posts = Post.objects.filter(category=category)
    return render(request, 'categories/category_detail.html', context={'posts': posts,
                                                                      'category':category,
                                                                      })
                                                                      
