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
            {"fields": ("name", "description", "country", "address", "price")}
        ),
        (
            "Times",
            {"fields": ("check_in","check_out","instant_book")}
        ),
        (
            "Spaces",
            {"fields": ("guests","beds","bedrooms","baths")}
        ),
        (
            "More About Space",
            {
                "classes": ("collapse",),
                "fields": ("amenities","facilities","house_rules"),
            }
        ),
        (
            "Last Details",
            {"fields": ("host",)}
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
        "house_rules",
        "city",
        "^host__username",
    )

    filter_horizontal = (
        "amenities",
        "facilities",
        "house_rules",
    )


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """ Definition Photo Admin """

    pass
