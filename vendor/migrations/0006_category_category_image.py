# Generated by Django 3.1.6 on 2021-02-08 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0005_auto_20210206_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_image',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
