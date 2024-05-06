from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from webinar.home.views import HomeView

admin_name = "Webinar Admin"
admin.site.site_header = admin_name
admin.site.site_title = admin_name

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path("", HomeView.as_view(), name="home"),
    # Django-RQ
    path(settings.RQ_URL, include("django_rq.urls")),
]


if settings.DEBUG:
    import debug_toolbar
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
