# Generated by Django 4.2 on 2023-05-28 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashb', '0011_alter_sortiemat1_date_retour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('ENCRE', 'ENCRE'), ('KIT BIMS', 'KIT BIMS'), ('IIMPRIMANTE', 'IMPRIMANTE'), ('SECURITE', 'SECURITE'), ('MAT RESEAU', 'MAT RESEAU'), ('MAT BUREAU', 'MAT BUREAU'), ('ORDINATEUR', 'ORDINATEUR')], max_length=25),
        ),
    ]