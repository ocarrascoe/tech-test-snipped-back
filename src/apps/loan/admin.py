from django.contrib import admin

from apps.loan.models import Loan


class LoanAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Loan._meta.get_fields()]


admin.site.register(Loan, LoanAdmin)

