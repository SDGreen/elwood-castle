from django.db import models
from django.core.validators import MaxValueValidator


# Create your models here.
class Category(models.Model):

    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=50, null=False, blank=False)
    friendly_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Event(models.Model):

    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=False)
    start_time = models.TimeField()
    rating = models.DecimalField(max_digits=2, decimal_places=1, null=True,
                                 blank=True)
    day_ticket_limit = models.PositiveIntegerField(blank=False,
                                                   validators=[
                                                       MaxValueValidator(200)
                                                   ])
    supervision = models.BooleanField(default=True, null=True, blank=True)
    age_restricted = models.BooleanField(default=True, null=True, blank=False)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
