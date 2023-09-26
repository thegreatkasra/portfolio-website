from django.contrib import admin
from django.urls import include, path
from django.contrib.sitemaps.views import sitemap
from website.sitemaps import BlogSitemap 


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
