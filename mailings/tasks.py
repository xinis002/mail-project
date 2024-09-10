import pytz
from django.conf import settings
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_job
from django.core.mail import send_mail
from django.utils import timezone
from .models import Mailing, MailingAttempt


def send_mailing():
    current_datetime = timezone.now()
    mailings = Mailing.objects.filter(
        start_datetime__lte=current_datetime, status="launched"
    )

    for mailing in mailings:
        last_attempt = mailing.attempts.order_by("-timestamp").first()
        if mailing.frequency == "daily" and (
            not last_attempt or (current_datetime - last_attempt.timestamp).days >= 1
        ):
            try:
                send_mail(
                    subject=mailing.message.subject,
                    message=mailing.message.body,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[client.email for client in mailing.clients.all()],
                )
                MailingAttempt.objects.create(mailing=mailing, status="success")
            except Exception as e:
                MailingAttempt.objects.create(mailing=mailing, status="failed")


def start():
    scheduler = BackgroundScheduler(timezone=pytz.timezone(settings.TIME_ZONE))
    scheduler.add_jobstore(DjangoJobStore(), "default")

    scheduler.add_job(send_mailing, "interval", minutes=10)

    scheduler.start()
    print("Scheduler started...")
