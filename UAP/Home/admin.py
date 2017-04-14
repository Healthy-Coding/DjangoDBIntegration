from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('timesent', 'subject', 'content', 'sender', 'resolved')
    list_editable = ('resolved',)
    date_hierarchy = 'timesent'
    list_filter = ('resolved',)
    ordering = ('timesent',)