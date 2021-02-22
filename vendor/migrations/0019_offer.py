# Generated by Django 3.1.6 on 2021-02-14 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0018_auto_20210213_1623'),
    ]

    operations = [
        migrations.CreateModel(
            name='offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer_name', models.CharField(blank=True, max_length=20, null=True)),
                ('offer_image', models.FileField(blank=True, max_length=255, null=True, upload_to='offers/offer_images')),
                ('offer_start', models.DateField(null=True)),
                ('offer_expiry', models.DateField(null=True)),
                ('discount_amount', models.FloatField(null=True)),
                ('Product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vendor.product')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vendor.category')),
            ],
        ),
    ]
