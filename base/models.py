from django.db import models


class Order(models.Model):
    inner_id = models.PositiveIntegerField(verbose_name='Inner ID', unique=True, null=False, blank=False)
    create_date = models.DateTimeField(auto_now=False)
    merchant = models.PositiveIntegerField(verbose_name='Merchant',  null=False, blank=False)
    status = models.CharField(verbose_name='Order status',  max_length=32, null=False, blank=False)
    amount = models.FloatField(verbose_name='Amount',  null=False, blank=False)
    currency = models.CharField(verbose_name='Currency', max_length=5,  null=False, blank=False)
    order_id = models.CharField(verbose_name='ID of order', max_length=64,  null=False, blank=False)
    order_type = models.CharField(verbose_name='Order type',  max_length=64, null=False, blank=False)
    description = models.TextField(verbose_name='Description',  null=True, blank=True)

    def __str__(self):
        return f'Order {self.id}'
