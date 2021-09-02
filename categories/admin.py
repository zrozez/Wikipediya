from django.contrib import admin
from categories.models import Category

class CategoryAdmin(admin.ModelAdmin):
    field = ['title', ]

admin.site.register(Category, CategoryAdmin)
