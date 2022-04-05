from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
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

    # get all comments assigned to post
    comments = get_object_or_404(Comment, post=post.id)


    # get all comments replies
    all_replies = []
    for comment in comments:
        replies = [get_object_or_404(Reply, comment=comment.id)]
        all_replies.append(replies)

    # template path and context
    template = 'posts/post_detail.html'
    context = {
        'post': post,
        'comments': comments,
        'replies': all_replies,
    }

    return render(request, template, context)