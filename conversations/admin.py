from django.contrib import admin
from . import models


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    """ Definition Message Admin """

    pass


@admin.register(models.Conversation)
class ConversationAdmin(admin.ModelAdmin):
    """ Definition Conversation Admin """

    pass
