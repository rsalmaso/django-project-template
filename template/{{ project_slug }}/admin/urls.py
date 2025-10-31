from django.contrib import admin as django_admin
from django.urls import include, path, re_path
from django.views import i18n as i18n_views

catalog_patterns = [
    re_path(r"^plain$", i18n_views.set_language, name="i18n"),
    re_path(r"^javascript/(?P<packages>\S+?)$", i18n_views.JavaScriptCatalog.as_view(), name="js"),
    re_path(r"^json/(?P<packages>\S+?)$", i18n_views.JSONCatalog.as_view(), name="json"),
]

urlpatterns = [
    path("i18n/", include((catalog_patterns, "i18n"))),
    path("", django_admin.site.urls),
]
