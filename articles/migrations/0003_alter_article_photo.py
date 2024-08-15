# Generated by Django 5.0.7 on 2024-08-10 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("articles", "0002_alter_article_is_publication_alter_article_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="photo",
            field=models.ImageField(
                blank=True,
                help_text="Загрузите превью статьи",
                null=True,
                upload_to="articles/article/photo",
                verbose_name="Фото",
            ),
        ),
    ]