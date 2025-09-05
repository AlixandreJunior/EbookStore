from django.db import models

from src.apps.user.models import Coupon, User
from src.apps.ebook.models import Ebook

class Order(models.Model):
    class Meta:
        app_label = "sales"
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    STATUS_CHOICES = [("pending","Pendente"),("paid","Pago"),("canceled","Cancelado")]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    coupon = models.ForeignKey(Coupon, null=True, blank=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return (f'Pedido ID: {self.pk}')

class OrderItem(models.Model):
    class Meta:
        app_label = "user"
        verbose_name = "Order Item"
        verbose_name_plural = "Order Itens"

    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    ebook = models.ForeignKey(Ebook, on_delete=models.CASCADE)
    final_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return (f'{self.ebook.title} do Pedido de ID: {self.order.pk}')