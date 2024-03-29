from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import home, service, portfolio, about, pricing, contact, blog


urlpatterns = [
    path('', home.index, name="index"),
    path('services', service.index, name="service"),

    path('portfolio', portfolio.index, name="portfolio"),
    path('portfolio/<str:slug>', portfolio.show, name="portfolio.show"),

    path('about', about.index, name="about"),
    path('pricing', pricing.index, name="pricing"),
    path('contact', contact.index, name="contact"),

    #blog
    path('blog', blog.index, name="blog.index"),
    path('blog/<str:slug>', blog.show, name="blog.show"),
    path('blog/category/<str:slug>', blog.category, name="blog.category"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
