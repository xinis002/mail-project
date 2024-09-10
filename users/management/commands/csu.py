from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        User = get_user_model()

        email = "admin@example.com"
        password = "adminpassword"

        if not User.objects.filter(email=email).exists():
            User.objects.create_superuser(
                email=email, password=password, is_staff=True, is_superuser=True
            )
            self.stdout.write(
                self.style.SUCCESS(f"Суперпользователь создан с email {email}")
            )
        else:
            self.stdout.write(
                self.style.WARNING(f"Суперпользователь с email {email} уже существует")
            )
