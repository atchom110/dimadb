# Generated by Django 4.2 on 2023-06-09 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashb', '0025_product_qte_sortie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('ENCRE', 'ENCRE'), ('ENCRE FARGO', 'ENCRE FARGO'), ('TONER', 'TONER'), ('KIT BIMS', 'KIT BIMS'), ('IMPRIMANTE', 'IMPRIMANTE'), ('SECURITE', 'SECURITE'), ('MAT RESEAU', 'MAT RESEAU'), ('MAT BUREAU', 'MAT BUREAU'), ('ENREGISTREMENT', 'ENREGISTREMENT'), ('ORDINATEUR', 'ORDINATEUR'), ('YTELEPHONE', 'TELEPHONE')], max_length=25),
        ),
    ]
