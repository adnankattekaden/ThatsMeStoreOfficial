# Generated by Django 3.1.6 on 2021-02-18 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0032_auto_20210218_1643'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='offer_type',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
