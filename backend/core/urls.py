
from django.contrib import admin
from django.urls import path, include  # add this
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)     # media files: photos, pdfs
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  # static files

urlpatterns += [
    # main pages
    path('admin/doc/', include('django.contrib.admindocs.urls')),               # django admin docs
    path('admin/', admin.site.urls),                                            # Django admin route
    path("", include("apps.authentication.urls")),                              # Auth routes - login / register
    path("", include("apps.home.urls")),
]
