from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from mailings.models import Mailing


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        manager_group, created = Group.objects.get_or_create(name="Менеджер")

        permissions = Permission.objects.filter(
            codename__in=["view_mailing", "view_user", "change_user", "delete_user"]
        )
        manager_group.permissions.set(permissions)
        self.stdout.write(
            self.style.SUCCESS("Группа Менеджер создана и права добавлены.")
        )
