# Generated by Django 5.0.4 on 2024-05-07 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bazar', '0003_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='anti_counterfeit_code',
        ),
        migrations.RemoveField(
            model_name='product',
            name='country_of_origin',
        ),
        migrations.RemoveField(
            model_name='product',
            name='manufacturer',
        ),
        migrations.RemoveField(
            model_name='product',
            name='production_date',
        ),
        migrations.RemoveField(
            model_name='product',
            name='seller',
        ),
        migrations.RemoveField(
            model_name='product',
            name='serial_number',
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
