from django.db import models

from . import PAYMENT_TYPES


class Payment(models.Model):
    """Тип оплаты."""

    payment_amount = models.BigIntegerField()
    payment_type = models.CharField(choices=PAYMENT_TYPES)
