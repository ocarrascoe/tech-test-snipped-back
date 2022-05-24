from django.contrib import admin

from apps.book.models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Book._meta.get_fields() if field.name != 'borrow']


admin.site.register(Book, BookAdmin)
