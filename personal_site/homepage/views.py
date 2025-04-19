from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


async def get_homepage(request: HttpRequest) -> HttpResponse:
    context = {
        "items": [1, 2, 3],
    }
    return render(
        request=request,
        template_name="homepage/home.html",
        context=context,
    )
