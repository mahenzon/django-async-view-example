from asyncio import TaskGroup

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from homepage.models import Profile
from homepage.services.currencies import get_exchange_rates
from homepage.services.jokes import get_single_joke


class HomePageView(TemplateView):
    extra_context = {
        "items": [1, 2, 3],
    }
    template_name = "homepage/home.html"


@login_required()
async def dashboard(request: HttpRequest) -> HttpResponse:
    async with TaskGroup() as tg:
        profile_task = tg.create_task(
            Profile.objects.select_related("user").aget(
                user=request.user,
            )
        )
        currencies_task = tg.create_task(
            get_exchange_rates(
                "rub",
                "jpy",
                "btc",
            )
        )
        joke_task = tg.create_task(get_single_joke())

    context = dict(
        profile=profile_task.result(),
        currencies=currencies_task.result(),
        joke=joke_task.result(),
    )
    return render(
        request=request,
        template_name="homepage/dashboard.html",
        context=context,
    )
