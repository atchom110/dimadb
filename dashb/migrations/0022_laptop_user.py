# Generated by Django 4.2 on 2023-06-08 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashb', '0021_alter_hightech_emplacement'),
    ]

    operations = [
        migrations.AddField(
            model_name='laptop',
            name='user',
            field=models.CharField(max_length=35, null=True),
        ),
    ]