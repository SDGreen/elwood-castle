from django.contrib import admin
from .models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name'
    )


# Register your models here.
admin.site.register(Category, CategoryAdmin)
