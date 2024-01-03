from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
admin.site.site_header = "NnaeziTech"
admin.site.site_title = "NnaeziTech"
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('nnaezi/', admin.site.urls),
    path("", include("nnaezitech.urls"))
]


if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
