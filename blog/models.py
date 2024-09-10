from django.db import models
from django.utils import timezone


class BlogPost(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержимое статьи")
    image = models.ImageField(
        upload_to="blog/images/", blank=True, null=True, verbose_name="Изображение"
    )
    views = models.PositiveIntegerField(default=0, verbose_name="Количество просмотров")
    publication_date = models.DateTimeField(
        default=timezone.now, verbose_name="Дата публикации"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ["-publication_date"]
