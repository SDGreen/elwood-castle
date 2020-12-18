from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import EventBooking


@receiver(post_save, sender=EventBooking)
def update_to_total(sender, instance, created, **kwargs):
    instance.order.update_total()


@receiver(post_delete, sender=EventBooking)
def delete_from_total(sender, instance, **kwargs):
    instance.order.update_total()
