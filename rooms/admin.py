from django.contrib import admin
from . import models


@admin.register(models.RoomType, models.Amenity, models.Facility, models.Rule)
class ItemAdmin(admin.ModelAdmin):
    """ Definition Item Admin """

    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """ DEFINITION ROOM ADMIN CLASS """

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "descripion", "country", "adress", "price")},
        ),
    )

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
    )

    list_filter = (
        "instant_book",
        "city",
        "country",
    )

    search_fields = (
        "instant_book",
        "host__superhost",
        "room_type",
        "amenities",
        "facilities",
        "house_rule",
        "city",
        "^host__username",
    )

    filter_horizontal = (
        "amenities",
        "facilities",
        "house_rule",
    )


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """ Definition Photo Admin """

    pass
