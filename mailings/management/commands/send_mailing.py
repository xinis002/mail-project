from django.core.management.base import BaseCommand
from mailings.tasks import send_mailing


class Command(BaseCommand):
    help = "Отправка рассылки"

    def handle(self, *args, **kwargs):
        send_mailing()
        self.stdout.write(self.style.SUCCESS("Успешно отправлены рассылки"))
