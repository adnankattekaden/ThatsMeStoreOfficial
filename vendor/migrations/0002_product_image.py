# Generated by Django 3.1.6 on 2021-02-04 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
