# Generated by Django 3.1.6 on 2021-02-21 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0043_offer_offer_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='wallet',
            name='cashback_amount',
            field=models.FloatField(default=0, null=True),
        ),
    ]