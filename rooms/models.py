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


class Photo(core_models.TimeStampedModel):
    """ Definition Photo Model """

    caption = models.CharField(max_length=80)
    file = models.ImageField()
    room = models.ForeignKey("Room",related_name="photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


class Room(core_models.TimeStampedModel):

    """Definition Room Class"""

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(user_models.User, related_name="rooms", on_delete=models.CASCADE)  # 1대 다
    room_type = models.ForeignKey(
        RoomType, related_name="rooms", on_delete=models.SET_NULL, null=True
    )  # 1대 다
    amenities = models.ManyToManyField(Amenity, related_name="rooms", blank=True)  # 다대 다 관계
    facilities = models.ManyToManyField(Facility, related_name="rooms", blank=True)
    house_rules = models.ManyToManyField(Rule, related_name="rooms", blank=True)

    def __str__(self):
        return self.name

    def total_rating(self):
        all_reviews = self.reviews.all()
        all_ratings = 0
        for review in all_reviews:
            all_ratings += review.rating_average()
        return all_ratings / len(all_reviews)

