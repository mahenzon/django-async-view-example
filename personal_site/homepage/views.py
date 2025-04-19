from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from homepage.models import Profile
from homepage.services.currencies import get_exchange_rates


class HomePageView(TemplateView):
    extra_context = {
        "items": [1, 2, 3],
    }
    template_name = "homepage/home.html"


@login_required()
async def dashboard(request: HttpRequest) -> HttpResponse:
    profile: Profile = await Profile.objects.select_related("user").aget(
        user=request.user,
    )
    currencies = await get_exchange_rates(
        "rub",
        "jpy",
        "btc",
    )
    context = dict(
        profile=profile,
        currencies=currencies,
    )
    return render(
        request=request,
        template_name="homepage/dashboard.html",
        context=context,
    )
