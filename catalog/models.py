from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование категории")
    description = models.TextField(
        verbose_name="Описание категории", blank=True, null=True
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование продукта")
    description = models.TextField(
        verbose_name="Описание продукта", blank=True, null=True
    )
    preview = models.ImageField(
        upload_to="prod/image",
        blank=True,
        null=True,
        verbose_name="Фотография продукта",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория продукта",
        blank=True,
        null=True,
        related_name='Продукты',
    )
    price = models.IntegerField(verbose_name="Цена продукта")
    created_at = models.DateField(
        auto_now_add=True, verbose_name="Дата создания (записи в БД)"
    )
    updated_at = models.DateField(
        auto_now=True, verbose_name="Дата последнего изменения (записи в БД)"
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "category", "price"]

    def __str__(self):
        return self.name
