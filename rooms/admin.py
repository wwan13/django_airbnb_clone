from django.contrib import admin
from . import models


@admin.register(models.RoomType, models.Amenity, models.Facility, models.Rule)
class ItemAdmin(admin.ModelAdmin):
    """ Definition Item Admin """

    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """ DEFINITION ROOM ADMIN CLASS """

    pass


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """ Definition Photo Admon """

    pass
