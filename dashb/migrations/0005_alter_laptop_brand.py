# Generated by Django 4.2 on 2023-05-10 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashb', '0004_alter_hightech_imei_alter_hightech_num_serie_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laptop',
            name='brand',
            field=models.CharField(choices=[('T14S GEN 1 (Lenovo)', 'T14S GEN 1 (Lenovo)'), ('T450S (Lenovo)', 'T450S (Lenovo)'), ('81HN (Lenovo)', '81HN (Lenovo)')], max_length=100),
        ),
    ]
