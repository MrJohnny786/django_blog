
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from league import views as league_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^articles/', include('articles.urls')),
    url(r'^league/', include('league.urls')),
    url(r'^about/$', views.about),
    url(r'^$', league_views.league_games, name = "home"),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
