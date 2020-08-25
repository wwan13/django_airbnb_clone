from django.contrib import admin
from django.utils.html import mark_safe
from . import models


@admin.register(models.RoomType, models.Amenity, models.Facility, models.Rule)
class ItemAdmin(admin.ModelAdmin):
    """ Definition Item Admin """

    list_didplay = (
        "name",
        "used_to",
    )


    def used_to(self,obj):
        return obj.rooms.count()


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
        "count_amenities",
        "count_photos",
        "total_rating",
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

    def count_amenities(self,obj):

        return obj.amenities.count()

    def count_photos(self,obj):

        return obj.photos.count()


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """ Definition Photo Admin """

    list_display = ("__str__","get_thumbnail")

    def get_thumbnail(self,obj):

        return mark_safe(f'<img width="70px" src = "{obj.file.url}">')
    get_thumbnail.short_description = "Thumbnail"