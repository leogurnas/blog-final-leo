from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from pages.views import home_view
from pages.views import about  



urlpatterns = [
    path('', home_view, name='home'), 
    path('admin/', admin.site.urls),
    path('pages/', include('pages.urls')),
    path('', include('accounts.urls')), 
    path('messages/', include('messenger.urls')),
    path('about/', about, name='about'),
    path('', include('pages.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


