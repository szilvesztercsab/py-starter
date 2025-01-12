"""Django app views."""

from django.http import HttpRequest, HttpResponse


def status(_: HttpRequest) -> HttpResponse:
    """Return a status message.

    Returns:
        HttpResponse: A status message.

    """
    return HttpResponse("OK")
