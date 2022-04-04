from parler.admin import TranslatableAdmin
from django.contrib import admin
from .models import *


@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Post)
class PostAdmin(TranslatableAdmin):
    list_display = ['title', 'category', 'author', 'status']
    list_editable = ['category', 'status']
    list_filter = ['category', 'author', 'status']
    search_fields = ['title']