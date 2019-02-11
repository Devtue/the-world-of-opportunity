from django.contrib import admin
from django.urls import path,include
from.import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('opportunity/',include('articles.urls')),
    path('',views.homepage,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('accounts/',include('accounts.urls')),
    path('', include('social_django.urls', namespace='social')),
]   
urlpatterns+=staticfiles_urlpatterns()
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)