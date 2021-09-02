from categories.views import categories_list_view
from django.urls import path
from categories.views import (categories_list_view, category_detail_view)
from posts.views import post_detail_view

urlpatterns = [
    path('', categories_list_view, name='categor_list_url'),
    path('<int:id>/', category_detail_view, name='category_detail_url'),
    path('<int:id>/post', post_detail_view, name='post_detail_url'),

]