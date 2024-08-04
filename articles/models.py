from django.db import models


class Article(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name="Заголовок",
        help_text="Введите заголовок статьи"
    )
    slug = models.CharField(
        max_length=50,
        verbose_name="Индефикатор"
    )
    description = models.TextField(
        verbose_name="Статья",
        help_text="Введите текст статьи",
        blank=True,
        null=True,
    )
    photo = models.ImageField(
        upload_to="product/photo",
        blank=True,
        null=True,
        verbose_name="Фото",
        help_text="Загрузите превью статьи",
    )
    created_at = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата написания статьи",
        help_text="Укажите дату написания статьи",
    )
    is_publication = models.BooleanField()
    count_views = models.IntegerField(
        default=0,
        verbose_name="Количество просмотров статьи",
    )

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

    def __str__(self):
        return self.title
