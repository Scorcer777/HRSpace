from django.contrib import admin

from .models import Payment
from utils import get_application_id


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'payment_amount', 'payment_type', 'application_id')
    application_id = get_application_id
