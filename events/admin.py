from django.contrib import admin
from .models import Category, Event


class EventAdmin(admin.ModelAdmin):

    list_display = (
        'pk',
        'name',
        'category',
        'price',
        'day_ticket_limit'
    )

    ordering = ('pk',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name'
    )


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Event, EventAdmin)
