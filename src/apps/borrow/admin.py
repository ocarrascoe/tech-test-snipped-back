from django.contrib import admin

from apps.borrow.models import Borrow


class BorrowAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Borrow._meta.get_fields()]


admin.site.register(Borrow, BorrowAdmin)

