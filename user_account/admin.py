from django.contrib import admin

from .models import UserAccount


# Register your models here.
class UserAccountAdmin(admin.ModelAdmin):

    class Meta:
        verbose_name_plural = "User Accounts"

    readonly_fields = ('user',)
    fields = ('user', ('first_name', 'last_name'), 'email', 'phone_number')


admin.site.register(UserAccount, UserAccountAdmin)
