from django.db import models
from django.utils import timezone

from django.contrib.auth import get_user_model

User = get_user_model()


class Client(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="clients", default=1
    )
    email = models.EmailField()
    full_name = models.CharField(max_length=255)
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"


class Message(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="messages", default=1
    )
    subject = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"


class Mailing(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="mailings", default=1
    )
    STATUS_CHOICES = [
        ("created", "Создана"),
        ("launched", "Запущена"),
        ("completed", "Завершена"),
    ]

    FREQUENCY_CHOICES = [
        ("daily", "Раз в день"),
        ("weekly", "Раз в неделю"),
        ("monthly", "Раз в месяц"),
    ]

    start_datetime = models.DateTimeField(
        default=timezone.now, verbose_name="Дата и время первой отправки"
    )
    frequency = models.CharField(
        max_length=10,
        choices=FREQUENCY_CHOICES,
        verbose_name="Периодичность",
        default="daily",
    )
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="created", verbose_name="Статус"
    )

    message = models.OneToOneField(
        "Message", on_delete=models.CASCADE, verbose_name="Сообщение"
    )
    clients = models.ManyToManyField(
        "Client", related_name="mailings", verbose_name="Клиенты"
    )

    def __str__(self):
        return f"Рассылка {self.pk} - {self.status}"

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"


class MailingAttempt(models.Model):
    mailing = models.ForeignKey(
        "Mailing", on_delete=models.CASCADE, related_name="attempts"
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=10, choices=[("success", "Успешно"), ("failed", "Неудачно")]
    )

    def __str__(self):
        return f"Попытка рассылки {self.mailing.id} - {self.status}"
