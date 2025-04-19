from django.contrib import admin

from homepage.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "birth_date",
        "city",
        "bio",
    )
