from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    extra_context = {
        "items": [1, 2, 3],
    }
    template_name = "homepage/home.html"


@login_required()
def dashboard(request: HttpRequest) -> HttpResponse:
    context = {}
    return render(
        request=request,
        template_name="homepage/dashboard.html",
        context=context,
    )
