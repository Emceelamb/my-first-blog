from django.conf.urls import include, url
from django.contrib import admin
from home import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls', namespace = "blog")),
    url(r'^portfolio/', include('portfolio.urls', namespace = "portfolio")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', ('home.views.homeImage')),
    url(r'^about/', ('home.views.about')),
    url(r'^contact/', ('home.views.contact')),
    
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
