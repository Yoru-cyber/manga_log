# Generated by Django 5.1.5 on 2025-01-26 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("manga_log_app", "0004_alter_item_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="category",
            field=models.CharField(
                choices=[("Manhwa", "Manhwa"), ("Manga", "Manga")],
                default="OTHER",
                max_length=10,
            ),
        ),
    ]
