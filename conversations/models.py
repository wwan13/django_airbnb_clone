from django.db import models
from core import models as core_models


class Conversation(core_models.TimeStampedModel):
    """ Definition Conversation Model """

    participants = models.ManyToManyField("users.User",related_name="conversation", blank=True)


class Message(core_models.TimeStampedModel):
    """ Definition Message Model """

    message = models.TextField()
    user = models.ForeignKey("users.User", related_name="messages" ,on_delete=models.CASCADE)
    conversation = models.ForeignKey("Conversation", related_name="messages", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} says: {self.text}"
