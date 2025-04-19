from django.urls import path

from homepage import views

app_name = "homepage"


urlpatterns = [
    path(
        "",
        views.HomePageView.as_view(),
        name="home",
    ),
    path(
        "dashboard/",
        views.dashboard,
        name="dashboard",
    ),
]
