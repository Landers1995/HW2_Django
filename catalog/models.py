from django.db import models

from users.models import User


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
    creator = models.ForeignKey(
        User,
        verbose_name='Создатель продукта',
        help_text='Укажите создателя продукта',
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )
    is_publication = models.BooleanField(
        verbose_name="Опубликовать?",
        default=False
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["category", "name"]
        permissions = [
            ('can_edit_description', 'Can edit description'),
            ('can_edit_category', 'Can edit category'),
            ('can_edit_is_publication', 'Can edit is publication')
        ]

    def __str__(self):
        return self.name


class Version(models.Model):
    product_name = models.ForeignKey(
        Product,
        verbose_name='Наименование продукта',
        related_name='version',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    number_version = models.PositiveIntegerField(
        default=0,
        verbose_name="Номер версии продукта",
        help_text="Введите номер версии продукта",
        blank=True,
        null=True,
    )
    name_version = models.CharField(
        max_length=50,
        verbose_name="Наименование версии продукта",
        help_text="Введите наименование версии продукта",
        blank=True,
        null=True,
    )
    indicates_current_version = models.BooleanField(
        verbose_name="признак текущей версии",
        help_text="Версия активна?",
        default=True
    )

    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = "Версии"
        ordering = ["product_name", 'number_version', "name_version"]

    def __str__(self):
        return self.name_version
