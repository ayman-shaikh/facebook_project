# Generated by Django 5.1.4 on 2024-12-20 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fb_app', '0002_remove_invoice_product_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='product_description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
