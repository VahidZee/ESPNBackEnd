"""EspnBackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
# General Imports
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Local Imports
from apps.News import urls as news_urls
from apps.Espn import urls as espn_urls
from apps.Comment import urls as comment_urls

from apps.Game import urls as g_url
# from apps.League import urls as l_url

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('news/', include(news_urls)),
                  path('users/', include(espn_urls)),
                  path('comment/', include(comment_urls)),
                  path('games/', include(g_url)),
                  # path('league/', include(l_url))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
