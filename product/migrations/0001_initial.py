# Generated by Django 5.0.2 on 2024-02-26 06:45

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
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'db_table': 'product_category',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_id', models.CharField(max_length=100)),
                ('discounted_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('actual_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount_percentage', models.IntegerField(default=0)),
                ('rating', models.DecimalField(decimal_places=2, max_digits=10)),
                ('rating_count', models.IntegerField(default=1)),
                ('about_product', models.TextField()),
                ('user_id', models.CharField(max_length=100)),
                ('user_name', models.CharField(max_length=100)),
                ('review_id', models.CharField(max_length=100)),
                ('review_title', models.CharField(max_length=100)),
                ('review_content', models.CharField(max_length=100)),
                ('img_link', models.CharField(max_length=100)),
                ('product_link', models.CharField(max_length=100)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.category')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
                'db_table': 'product_product',
                'ordering': ('-id',),
            },
        ),
    ]
