from django.utils.translation import gettext as _
from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path(_('category/<int:id>/'), views.posts_by_category, name='posts_by_category'),
    path(_('blog/<int:id>/'), views.post_detail, name='post_detail'),
    path(_('search/'), views.search, name='search'),
]