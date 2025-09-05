from django.db import models
from src.apps.user.models import User
from src.apps.sales.models.order import OrderItem

class Commission(models.Model):
    class Meta:
        app_label = "sales"
        verbose_name = "Comissão"
        verbose_name_plural = "Comissões"

    affiliate = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={"role": "affiliate"},
        verbose_name="Afiliado"
    )
    order_item = models.ForeignKey(
        OrderItem,
        on_delete=models.CASCADE,
        verbose_name="Item do Pedido"
    )
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Valor da Comissão"
    )
    paid = models.BooleanField(
        default=False,
        verbose_name="Pago"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Criado em"
    )

    def __str__(self):
        return f"{self.affiliate.username} - Comissão {self.amount} do Pedido ID: {self.order_item.order.pk} ({'Pago' if self.paid else 'Pendente'})"
