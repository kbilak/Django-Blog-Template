"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.utils.translation import gettext as _
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from django.contrib import admin

urlpatterns = i18n_patterns(
    # Admin panel
    path(_('admin/'), admin.site.urls),

    # Translations
    path('rosetta/', include('rosetta.urls')),

    # User management
    path(_('accounts/'), include('allauth.urls')),

    # Apps
    path(_('accounts/'), include('accounts.urls')),
    path(_('blog/'), include('posts.urls')),
    path('', include('page.urls')),
) 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
