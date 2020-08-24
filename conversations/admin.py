from django.contrib import admin
from . import models


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    """ Definition Message Admin """

    list_display = ("__str__","created")


@admin.register(models.Conversation)
class ConversationAdmin(admin.ModelAdmin):
    """ Definition Conversation Admin """

    list_display = ("__str__","count_messages","count_participants")