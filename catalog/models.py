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
        return f'{self.name}'


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

    views_counter = models.PositiveIntegerField(
        verbose_name="Счётчик просмотров",
        help_text='Проказывает кол-во просмотров',
        default=0
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "category", "price"]

    def __str__(self):
        return f'{self.name}'


class Version(models.Model):
    product = models.ForeignKey(Product, related_name='Продукт', on_delete=models.SET_NULL, null=True, blank=True)
    version_number = models.PositiveIntegerField(verbose_name='Номер версии', default=0)
    version_name = models.TextField(verbose_name='Название версии')
    current_version = models.BooleanField(verbose_name='Версия для отображения на сайте')

    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = "Версии"
        ordering = ["product", "version_number", "version_name", "current_version"]

    def __str__(self):
        return f'{self.product}'
