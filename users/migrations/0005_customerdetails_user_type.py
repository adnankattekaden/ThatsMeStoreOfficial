# Generated by Django 3.1.6 on 2021-02-21 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_customerdetails_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerdetails',
            name='user_type',
            field=models.CharField(blank=True, default='DirectUser', max_length=10),
        ),
    ]
