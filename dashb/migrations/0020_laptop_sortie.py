# Generated by Django 4.2 on 2023-06-04 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashb', '0019_hightech_sortie'),
    ]

    operations = [
        migrations.AddField(
            model_name='laptop',
            name='sortie',
            field=models.CharField(choices=[('OUI', 'OUI'), ('NON', 'NON')], max_length=25, null=True),
        ),
    ]
