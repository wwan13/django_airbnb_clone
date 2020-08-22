from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models


class AbstractItem(core_models.TimeStampedModel):

    """ Abstract Item """

    name = models.CharField(max_length=80)

    class meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):
    """ Definition Room Type """

    class Meta:
        verbose_name = "Room Type"


class Amenity(AbstractItem):
    """ Definition Room Type """

    class Meta:
        verbose_name_plural = "Amenities"


class Facility(AbstractItem):
    """ Definition Facility """

    class Meta:
        verbose_name_plural = "Facilities"


class Rule(AbstractItem):
    """ Definition House Rule """

    class Meta:
        verbose_name = "House Rule"


class Room(core_models.TimeStampedModel):

    """Definition Room Class"""

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    adress = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(user_models.User, on_delete=models.CASCADE)  # 1대 다
    room_type = models.ForeignKey(
        RoomType, on_delete=models.SET_NULL, null=True
    )  # 1대 다
    amenities = models.ManyToManyField(Amenity, blank=True)  # 다대 다 관계
    facilities = models.ManyToManyField(Facility, blank=True)
    house_rule = models.ManyToManyField(Rule, blank=True)

    def __str__(self):
        return self.name


class Photo(core_models.TimeStampedModel):
    """ Definition Photo Model """

    caption = models.CharField(max_length=80)
    file = models.ImageField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return self.caption
