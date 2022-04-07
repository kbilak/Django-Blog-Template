from django.utils.translation import gettext as _
from django.urls import path
from . import views

app_name = 'opage'

urlpatterns = [
    path('', views.index, name='index'),
]