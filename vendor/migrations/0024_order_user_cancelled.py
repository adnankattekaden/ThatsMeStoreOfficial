# Generated by Django 3.1.6 on 2021-02-18 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0023_order_discounted'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='user_cancelled',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
