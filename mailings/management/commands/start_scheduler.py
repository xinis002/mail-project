from django.core.management.base import BaseCommand
from mailings.tasks import start  # Импортируем функцию, запускающую планировщик


class Command(BaseCommand):
    help = "Запуск планировщика задач для рассылок"

    def handle(self, *args, **kwargs):
        start()
        self.stdout.write(self.style.SUCCESS("Планировщик задач успешно запущен"))
