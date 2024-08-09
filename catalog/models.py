from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Категория",
        help_text="Введите наименование категории",
    )
    description = models.TextField(
        verbose_name="Описание категории",
        help_text="Введите описание категории",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Наименование",
        help_text="Введите наименование продукта",
    )
    description = models.TextField(
        verbose_name="Описание продукта",
        help_text="Введите описание продукта",
        blank=True,
        null=True,
    )
    photo = models.ImageField(
        upload_to="product/photo",
        blank=True,
        null=True,
        verbose_name="Фото",
        help_text="Загрузите фото продукта",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        help_text="Введите категорию продукта",
        blank=True,
        null=True,
        related_name='products',
    )
    price = models.IntegerField(
        default=0,
        verbose_name="Цена продукта",
        help_text="Введите цену продукта",
    )
    # manufactured_at = models.DateField(
    #     blank=True,
    #     null=True,
    #     verbose_name="Дата производства продукта",
    #     help_text="Укажите дату производства продукта",
    # )
    created_at = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата создания продукта",
        help_text="Укажите дату создания продукта",
    )
    updated_at = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата последнего изменения продукта",
        help_text="Укажите дату последнего изменения продукта",
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["category", "name"]

    def __str__(self):
        return self.name
