from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from .models import *


"""
Blog's index page view
"""
def index(request):
    # get all posts that are 'published'
    posts = Post.objects.filter(status='2')
    
    # set default ammount of posts per page to 10
    paginator = Paginator(posts, 10)

    # paginator config
    page = request.GET.get('p')
    venues = paginator.get_page(page)

    # template path and context
    template = 'posts/index.html'
    context = {
        'venues': venues,
    }

    return render(request, template, context)


"""
Post list by category
"""
def posts_by_category(request, id):
    # get all posts with given category
    posts = Post.objects.filter(category__id=id)

    # set default ammount of posts per page to 10
    paginator = Paginator(posts, 10)

    # paginator config
    page = request.GET.get('p')
    venues = paginator.get_page(page)

    # template path and context
    template = 'posts/posts_by_category.html'
    context = {
        'venues': venues,
    }

    return render(request, template, context)


"""
Post detail view
"""
def post_detail(request, id):
    # get post by id
    post = get_object_or_404(Post, id=id)

    # get all reviews of post
    reviews = get_object_or_404(Review, post=post)

    # get all comments assigned to post
    comments = get_object_or_404(Comment, post=post)

    # get all comments replies
    all_replies = []
    for comment in comments:
        replies = [get_object_or_404(Reply, comment=comment.id)]
        all_replies.append(replies)

    # template path and context
    template = 'posts/post_detail.html'
    context = {
        'post': post,
        'reviews': reviews,
        'comments': comments,
        'replies': all_replies,
    }

    return render(request, template, context)

"""
Search engine
"""
def search(request):
    query = request.GET.get('q')

    # filter published posts
    search_result = Post.objects.filter(
        status='2' and 
        Q(translations__title__icontains=query) | 
        Q(translations__body__icontains=query) | 
        Q(category__icontains=query) | 
        Q(author__icontains=query) |
        Q(tags__icontains=query)
    )
    # set default ammount of results per page to 10
    paginator = Paginator(search_result, 10)

    # paginator config
    page = request.GET.get('p')
    venues = paginator.get_page(page)

    # template path and context
    template = 'posts/search_result.html'
    context = {
        'venues': venues,
    }

    return render(request, template, context)
