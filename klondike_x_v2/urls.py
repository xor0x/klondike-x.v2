
from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap
from blog import views
from django.conf.urls.static import static
from django.conf import settings


sitemaps = {
    'posts':PostSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.post_list, name='home'),
    path('blog/', include('blog.urls', namespace='blog')),
    path('sitemap.xml', sitemap, {'sitemaps':sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('account/', include('accounts.urls')),
    path('account/', include('django.contrib.auth.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
