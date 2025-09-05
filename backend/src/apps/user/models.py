from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

from src.utils.validates import validate_br_phone, validate_cpf


class UsersManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("O e-mail é obrigatório!")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    class Meta:
        app_label = "user"
        verbose_name = "User"
        verbose_name_plural = "Users"

    USER_ROLES = [
        ("client", "Cliente"),
        ("affiliate", "Afiliado"),
        ("supporter", "Supporter"),
    ]
    
    role = models.CharField(max_length=20, choices=USER_ROLES, default="client")
    phone = models.CharField(max_length=15, unique=True, validators=[validate_br_phone])
    cpf = models.CharField(max_length=11, unique=True, validators=[validate_cpf]
)
    photo = models.ImageField(upload_to="users/photos/", blank=True, null=True)

    def __str__(self):
        return self.username

class Coupon(models.Model):
    class Meta:
        app_label = "user"
        verbose_name = "Coupon"
        verbose_name_plural = "Coupons"

    code = models.CharField(max_length=20, unique=True)
    affiliate = models.ForeignKey(User, on_delete=models.CASCADE, related_name="coupons")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f'Cupom de {self.affiliate.username}')