from django.urls import path, include
from django.contrib import admin
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('devices/', include('websiteapp.urls'), name='list_devices'),
    path('api/', include('notification_system.urls'), name='api-main'),
    path('', RedirectView.as_view(pattern_name='websiteapp:integration', permanent=False))
]



from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
