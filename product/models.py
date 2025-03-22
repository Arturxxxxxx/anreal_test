from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=50, unique=True, verbose_name='Категория')

    def __str__(self):
        return self.category

class ProductHome(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product/')
    title = models.CharField(max_length=100, verbose_name='название')
    address = models.CharField(max_length=100, verbose_name='адрес')
    year = models.PositiveBigIntegerField(verbose_name='год')

    def __str__(self):
        return self.title

