
from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap
from blog import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns


sitemaps = {
    'posts':PostSitemap,
}

urlpatterns = i18n_patterns(
    path('admin-dashboard/', admin.site.urls),
    path('rosetta/', include('rosetta.urls')),
    path('',views.post_list, name='home'),
    path('blog/', include('blog.urls', namespace='blog')),
    path('about/', views.about, name='about'),
    path('sitemap.xml', sitemap, {'sitemaps':sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('account/', include('accounts.urls')),
    path('account/', include('django.contrib.auth.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
