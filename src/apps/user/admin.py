from django.contrib import admin

from apps.user.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = [field.name for field in User._meta.get_fields() if field.name != 'borrow']


admin.site.register(User, UserAdmin)
