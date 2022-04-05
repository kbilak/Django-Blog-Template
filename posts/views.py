from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import *


"""
Blog's index page view
"""
def index(request):
    posts = Post.objects.all()
    
    # set default ammount of posts per page to 10
    paginator = Paginator(posts, 10)

    # paginator config
    page = request.GET.get('page')
    venues = paginator.get_page(page)

    # template path and context
    template = 'posts/index.html'
    context = {
        'venues': venues,
    }

    return render(request, template, context)
