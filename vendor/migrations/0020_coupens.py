# Generated by Django 3.1.6 on 2021-02-15 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0019_offer'),
    ]

    operations = [
        migrations.CreateModel(
            name='coupens',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coupen_name', models.CharField(blank=True, max_length=255, null=True)),
                ('coupen_code', models.CharField(blank=True, max_length=20, null=True)),
                ('validity_starts', models.DateField(null=True)),
                ('validity_expire', models.DateField(null=True)),
                ('coupen_status', models.BooleanField(default=False)),
            ],
        ),
    ]
