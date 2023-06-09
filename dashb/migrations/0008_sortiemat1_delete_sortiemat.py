# Generated by Django 4.2 on 2023-05-27 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashb', '0007_laptop_imei'),
    ]

    operations = [
        migrations.CreateModel(
            name='sortieMat1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=50, null=True)),
                ('quantity', models.PositiveIntegerField(null=True)),
                ('decharge', models.CharField(max_length=50, null=True)),
                ('info', models.CharField(max_length=80, null=True)),
                ('duree', models.CharField(choices=[('TEMPORAIRE', 'TEMPORAIRE'), ('DEFINITIF', 'DEFINITIF')], max_length=25, null=True)),
                ('date_sortie', models.DateTimeField(null=True)),
                ('retour', models.CharField(choices=[('OUI', 'OUI'), ('NON', 'NON')], max_length=25, null=True)),
                ('date_retour', models.DateTimeField(null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='SortieMat',
        ),
    ]