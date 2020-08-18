from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)  # admin.site.register(user)과 같은 의미
class CustomUserAdmin(UserAdmin):
    """Custom User Admin"""

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "language",
                    "birthdate",
                    "currency",
                    "superhost",
                )
            },
        ),
    )


# 어우 개복잡해 미친건가
# 튜플 안에 튜플 안에 리스트 안에 튜플 ?

# list_display = ("보여질거 1", "보여질거 2")
# list_filter = ("나눌꺼",)
