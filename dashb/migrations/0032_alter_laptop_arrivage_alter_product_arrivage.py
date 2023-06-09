# Generated by Django 4.2 on 2023-06-09 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashb', '0031_alter_product_arrivage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laptop',
            name='arrivage',
            field=models.CharField(choices=[('NEUF', 'NEUF'), ('OUI', 'OUI'), ('NON', 'NON')], max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='arrivage',
            field=models.CharField(choices=[('OUI', 'OUI'), ('NON', 'NON')], max_length=25, null=True),
        ),
    ]
