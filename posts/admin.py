from parler.admin import TranslatableAdmin
from django.contrib import admin
from .models import *


class RevievInline(admin.TabularInline):
    model = Review


class CommentInline(admin.TabularInline):
    model = Comment


class ReplyInline(admin.TabularInline):
    model = Reply


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
    inlines = [RevievInline, CommentInline]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'author', 'active', 'created', 'updated']
    list_filter = ['author', 'active']
    search_fields = ['author', 'post', 'body']
    inlines = [ReplyInline]


@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    list_display = ['comment', 'author', 'active', 'created', 'updated']
    list_filter = ['author', 'active']
    search_fields = ['author', 'post', 'body']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['post', 'author', 'rate', 'active', 'created', 'updated']