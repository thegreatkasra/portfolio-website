from django.contrib import admin
from django.urls import include, path
from django.contrib.sitemaps.views import sitemap
from website.sitemaps import BlogSitemap 
from django.conf import settings
from django.conf.urls.static import static


sitemaps = {
    'posts': BlogSitemap,
}


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('captcha/', include('captcha.urls')),                  #captcha config url
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),  #Sitemap
    path('robots.txt', include('robots.urls')),      #robot SEO url
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)