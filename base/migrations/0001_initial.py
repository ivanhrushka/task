# Generated by Django 2.1.2 on 2018-10-10 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inner_id', models.PositiveIntegerField(unique=True, verbose_name='Inner ID')),
                ('create_date', models.DateTimeField()),
                ('merchant', models.PositiveIntegerField(verbose_name='Merchant')),
                ('status', models.CharField(max_length=32, verbose_name='Order status')),
                ('amount', models.FloatField(verbose_name='Amount')),
                ('currency', models.CharField(max_length=5, verbose_name='Currency')),
                ('order_id', models.CharField(max_length=64, verbose_name='ID of order')),
                ('order_type', models.CharField(max_length=64, verbose_name='Order type')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
            ],
        ),
    ]
