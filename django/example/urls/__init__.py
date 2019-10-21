import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from example.urls import web, api

urlpatterns = [
    path("__debug__/", include(debug_toolbar.urls)),
    path("api/", include(api)),
    path("", include(web)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
