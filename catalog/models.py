from django.db import models


class Category(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Наименование категории",
        help_text="Укажите название категории",
    )
    description = models.TextField(
        verbose_name="Описание категории",
        help_text="Добавьте описание категории",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["title"]

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование продукта",
        help_text="Укажите название продукта",
    )
    description = models.TextField(
        verbose_name="Описание продукта",
        help_text="Добавьте описание продукта",
        blank=True,
        null=True,
    )
    image = models.ImageField(
        upload_to="catalog/images",
        blank=True,
        null=True,
        verbose_name="Фото",
        help_text="Загрузите изображение товара",
    )
    category = models.ForeignKey(
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Категория",
        related_name="products",
        to="Category",
    )
    price = models.FloatField(
        verbose_name="Цена", help_text="Укажите стоимость продукта"
    )
    created_at = models.DateField(
        auto_now_add=True,
        verbose_name="Дата создания продукта",
        help_text="Добавьте дату создания продукта",
    )
    updated_at = models.DateField(
        auto_now=True,
        verbose_name="Дата последнего изменения продукта",
        help_text="Добавьте дату изменения продукта",
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "price"]

    def __str__(self):
        return self.name


class Version(models.Model):
    product = models.ForeignKey(
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Продукт",
        related_name="versions",
        to="Product",
    )
    version_number = models.PositiveIntegerField(
        verbose_name="Номер версии",
        help_text="Укажите номер версии продукта",
    )
    version_name = models.CharField(
        max_length=100,
        verbose_name="Наименование версии",
        help_text="Укажите название версии",
    )
    is_current_version = models.BooleanField(
        verbose_name="Текущая версия",
        help_text="Укажите, является ли текущей версией продукта",
        default=False,
    )

    class Meta:
        verbose_name = "Версия продукта"
        verbose_name_plural = "Версии продуктов"
        ordering = ["-version_number"]

    def __str__(self):
        return f"{self.product.name} - {self.version_number} {self.version_name}"
