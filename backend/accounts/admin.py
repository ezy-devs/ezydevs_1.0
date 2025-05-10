from django.contrib import admin
from .models import *


# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'location', 'birth_date', 'website', 'phone_number')
    search_fields = ('user__email', 'location')
    list_filter = ('birth_date',)
    ordering = ('-birth_date',)
    fieldsets = (
        (None, {
            'fields': ('user', 'bio', 'location')
        }),
        ('Additional Info', {
            'fields': ('birth_date', 'website', 'phone_number')
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('user', 'bio', 'location', 'birth_date', 'website', 'phone_number')
        }),
    )
    readonly_fields = ('user',)


