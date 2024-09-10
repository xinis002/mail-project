from django.contrib import admin
from .models import Client, Message, Mailing, MailingAttempt


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "comment")
    search_fields = ("full_name", "email")
    list_filter = ("email",)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("subject", "body")
    search_fields = ("subject",)


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ("id", "start_datetime", "status", "frequency", "message")
    list_filter = ("status", "frequency")
    search_fields = ("message__subject",)
    filter_horizontal = ("clients",)


@admin.register(MailingAttempt)
class MailingAttemptAdmin(admin.ModelAdmin):
    list_display = ("mailing", "timestamp", "status")
    list_filter = ("status",)
    search_fields = ("mailing__id",)
