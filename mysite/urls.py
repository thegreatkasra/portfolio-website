from django.contrib import admin
from django.urls import include, path
#from django.contrib.sitemaps.views import sitemap
#from blog.sitemaps import PostSitemap 
#from robots.views import RuleList

""" sitemaps = {
    'posts': PostSitemap,
} """


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('captcha/', include('captcha.urls')),                  #captcha config url
    #path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),  #Sitemap
    #path("robots.txt", RuleList.as_view(), name="robots"),      #robot SEO url
]
