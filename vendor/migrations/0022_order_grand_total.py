# Generated by Django 3.1.6 on 2021-02-17 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0021_coupens_discount_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='grand_total',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
