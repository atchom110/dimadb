# Generated by Django 4.2 on 2023-05-28 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashb', '0012_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('ENCRE', 'ENCRE'), ('KIT BIMS', 'KIT BIMS'), ('IMPRIMANTE', 'IMPRIMANTE'), ('SECURITE', 'SECURITE'), ('MAT RESEAU', 'MAT RESEAU'), ('MAT BUREAU', 'MAT BUREAU'), ('ENREGISTREMENT', 'ENREGISTREMENT'), ('ORDINATEUR', 'ORDINATEUR')], max_length=25),
        ),
    ]