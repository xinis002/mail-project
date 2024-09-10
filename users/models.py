from django.contrib.auth.models import AbstractUser
from django.db import models

from users.managers import CustomUserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True, verbose_name="Email", help_text="Write email"
    )
    phone = models.CharField(
        max_length=35,
        verbose_name="Phone",
        blank=True,
        null=True,
        help_text="Enter phone number in format +7-XXX-XXX-XXXX",
    )
    city = models.CharField(
        max_length=50,
        verbose_name="City",
        blank=True,
        null=True,
        help_text="Enter city",
    )
    avatar = models.ImageField(
        upload_to="users/avatars/",
        verbose_name="Avatar",
        blank=True,
        null=True,
        help_text="Upload avatar",
    )

    token = models.CharField(
        max_length=100, verbose_name="Token", blank=True, null=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
