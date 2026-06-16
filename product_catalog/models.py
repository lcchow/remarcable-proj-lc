from django.db import models

MAX_SHORT_LENGTH = 50
MAX_LONG_LENGTH = 200

class Category(models.Model):
    name = models.CharField(max_length=MAX_SHORT_LENGTH)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=MAX_SHORT_LENGTH)

    def __str__(self):
        return self.name 


class Product(models.Model):
    description = models.CharField(max_length=MAX_LONG_LENGTH)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')
    tags = models.ManyToManyField(Tag, related_name='products')

    def __str__(self):
        return self.description 