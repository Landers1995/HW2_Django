# Generated by Django 4.2.2 on 2024-08-22 11:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("catalog", "0006_alter_version_product_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="creator",
            field=models.ForeignKey(
                blank=True,
                help_text="Укажите создателя продукта",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Создатель продукта",
            ),
        ),
    ]
