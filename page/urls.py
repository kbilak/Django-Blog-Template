from django.utils.translation import gettext as _
from django.urls import path
from . import views

app_name = 'page'

urlpatterns = [
    path('', views.index, name='index'),
    path(_('terms-and-conditions/'), views.terms_and_conditions, name='terms_and_conditions'),
    path(_('cookies/'), views.cookies, name='cookies'),
    path(_('about/'), views.about, name='about'),
    path(_('contact/'), views.contact, name='contact'),
]