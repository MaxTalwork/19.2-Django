# Generated by Django 5.0.6 on 2024-07-07 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0005_alter_product_description"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="version",
            options={
                "ordering": [
                    "product",
                    "version_number",
                    "version_name",
                    "current_version",
                ],
                "verbose_name": "Версия",
                "verbose_name_plural": "Верси",
            },
        ),
        migrations.AlterField(
            model_name="product",
            name="description",
            field=models.TextField(
                blank=True, null=True, verbose_name="Описание продукта"
            ),
        ),
        migrations.AlterField(
            model_name="version",
            name="current_version",
            field=models.BooleanField(verbose_name="Версия для отображения на сайте"),
        ),
    ]