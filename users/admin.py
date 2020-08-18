from django.contrib import admin
from . import models


@admin.register(models.User)  # admin.site.register(user)과 같은 의미
class CustomUserAdmin(admin.ModelAdmin):
    """Custom User Admin"""

    list_display = ("username", "gender", "language", "currency", "superhost")
    list_filter = ("language", "currency", "superhost")
