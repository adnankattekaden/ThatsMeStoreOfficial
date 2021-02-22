# Generated by Django 3.1.6 on 2021-02-19 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0038_auto_20210219_0600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='offer_percentage',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='offer_price',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]