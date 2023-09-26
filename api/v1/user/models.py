from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from api.v1.utile.models import CustomAbstractModel
from .manager import CustomManager

class User(AbstractBaseUser, PermissionsMixin, CustomAbstractModel):
    first_name = models.CharField(max_length=255, help_text="Ism")
    last_name = models.CharField(max_length=255, help_text="Familiya")
    phone = models.CharField(max_length=13, unique=True, help_text="Telfon raqam")
    email = models.CharField(max_length=255, blank=True, null=True)

    is_staff = models.BooleanField(default=False)

    objects = CustomManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ("first_name", "last_name",)

    def __str__(self) -> str:
        return f"{self.first_name} {self.phone}"
