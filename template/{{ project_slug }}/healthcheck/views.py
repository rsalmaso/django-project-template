from django.contrib.auth import get_user_model
from django.http import HttpRequest, HttpResponse


def healthy(request: HttpRequest) -> HttpResponse:
    status: int = 200
    try:
        get_user_model().objects.count()
    except:
        status = 500
    return HttpResponse(status=status)
