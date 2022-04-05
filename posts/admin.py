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


@admin.register(Comment)
class CommentAdmin(TranslatableAdmin):
    list_display = ['post', 'author', 'active', 'created', 'updated']
    list_filter = ['author', 'active']
    search_fields = ['author', 'post', 'body']


@admin.register(Reply)
class ReplyAdmin(TranslatableAdmin):
    list_display = ['comment', 'author', 'active', 'created', 'updated']
    list_filter = ['author', 'active']
    search_fields = ['author', 'post', 'body']


@admin.register(Review)
class ReviewAdmin(TranslatableAdmin):
    list_display = ['post', 'author', 'rate', 'active', 'created', 'updated']