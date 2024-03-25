import statistics
from django.conf import settings
from django.urls import URLPattern, include, path
from django.views.generic import RedirectView
from locallibrary.catalog import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),
    path('', RedirectView.as_view(url='catalog/')),
] + statistics(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
