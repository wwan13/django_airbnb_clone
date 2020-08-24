from django.db import models
from django.utils import timezone
from core import models as core_models


class Reservation(core_models.TimeStampedModel):
    """ Definition Reservation Model """

    STATUS_PENDING = "Pending"
    STATUS_CONFIRMED = "confirmed"
    STATUS_CANCELED = "canceled"

    STATUS_CHOICES = (
        (STATUS_PENDING, "Pending"),
        (STATUS_CONFIRMED, "Confirmed"),
        (STATUS_CANCELED, "Canceled"),
    )

    status = models.CharField(
        choices=STATUS_CHOICES, max_length=12, default=STATUS_PENDING
    )
    guest = models.ForeignKey("users.User",related_name="reservations", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room",related_name="reservations", on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()

    def in_progress(self):
        now = timezone.now().date()
        return now > self.check_in and now < self.check_out
        
    in_progress.boolean = True 

    def is_finished(self):
        now = timezone.now().date()
        return now > self.check_out
    
    is_finished.boolean = True