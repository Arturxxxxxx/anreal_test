# Generated by Django 5.1.6 on 2025-03-21 15:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50, unique=True, verbose_name='Категория')),
            ],
        ),
        migrations.CreateModel(
            name='ProductHome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product/')),
                ('title', models.CharField(max_length=100, verbose_name='название')),
                ('address', models.CharField(max_length=100, verbose_name='адрес')),
                ('year', models.PositiveBigIntegerField(verbose_name='год')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.category')),
            ],
        ),
    ]
