from django.contrib import admin
from .models import EventBooking, Order


class EventBookingAdmin(admin.ModelAdmin):

    readonly_fields = ('confirmation_number', 'order', 'booking_total')
    fields = (('confirmation_number', 'order'), ('event', 'date'),
              'ticket_quantity', 'booking_total')


class EventBookingAdminInline(admin.TabularInline):
    model = EventBooking
    readonly_fields = ('confirmation_number', 'booking_total')


class OrderAdmin(admin.ModelAdmin):

    inlines = (EventBookingAdminInline,)

    readonly_fields = ('order_number', 'date', 'total', 'stripe_id',
                       'user_account',)

    fields = (('order_number', 'date'), 'user_account', ('first_name',
              'last_name'), ('email', 'phone_number'), 'stripe_id', 'total',)


# Register your models here.
admin.site.register(EventBooking, EventBookingAdmin)
admin.site.register(Order, OrderAdmin)
