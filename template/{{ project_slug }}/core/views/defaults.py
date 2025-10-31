from django.http import HttpRequest, HttpResponse
from django.views import defaults as default_views
from django.views.decorators.csrf import requires_csrf_token


@requires_csrf_token
def bad_request(request: HttpRequest, exception: str, template_name: str = "400.html") -> HttpResponse:
    return default_views.bad_request(request, exception, template_name)


@requires_csrf_token
def permission_denied(request: HttpRequest, exception: str, template_name: str = "403.html") -> HttpResponse:
    return default_views.permission_denied(request, exception, template_name)


@requires_csrf_token
def page_not_found(request: HttpRequest, exception: str, template_name: str = "404.html") -> HttpResponse:
    return default_views.page_not_found(request, exception, template_name)


@requires_csrf_token
def server_error(request: HttpRequest, template_name: str = "500.html") -> HttpResponse:
    return default_views.server_error(request, template_name)
