import logging

from django.db import models, transaction
from user.models import User, Address
from product.models import Basket

logger = logging.getLogger('order_logger')


class Order(models.Model):
    STATUSES = (
        ('created', 'Created'),
        ('paid', 'Paid'),
        ('on_way', 'On way'),
        ('delivered', 'Delivered'),
        ('canceled', 'Canceled')
    )

    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    address = models.ForeignKey(to=Address, on_delete=models.SET_NULL, null=True)
    basket_history = models.JSONField(default=dict)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, default='created', choices=STATUSES)
    initiator = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Order #{self.id}. {self.first_name} {self.last_name}'

    def update_after_payment(self):
        baskets = Basket.objects.filter(user=self.initiator)
        self.status = 'paid'
        self.basket_history = {
            'purchased_items': [basket.de_json() for basket in baskets],
            'total_sum': float(baskets.total_sum()),
        }
        logger.info({
            'order_id': self.id,
            'user': self.initiator,
            'total_sum': float(baskets.total_sum()),
        })
        with transaction.atomic():
            for basket in baskets:
                product = basket.product
                product.quantity -= basket.quantity
                product.save()
        baskets.delete()
        self.save()

