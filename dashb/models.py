from django.db import models

# Create your models here.
class Category(models.Model):
    CATEGORY = (
        ('ENCRE', 'ENCRE'),
        ('KIT BIMS', 'KIT BIMS'),
        ('IIMPRIMANTE', 'IMPRIMANTE'),
        ('SECURITE', 'SECURITE'),
        ('MAT BUREAU', 'MAT BUREAU'),
        ('ORDINATEUR', 'ORDINATEUR'),
    )
    name = models.CharField(max_length=25, choices=CATEGORY)

    def __str__(self):
        return self.name

class Product(models.Model):
    EMPLACEMENT = (
        ('SALLE SPORT','SALLE SPORT'),
        ('SALLE SERVEUR','SALLE SERVEUR'),
        ('CENTRE TRANSIT', 'CENTRE TRANSIT'),
        ('MINAWAO', 'MINAWAO'),
        ('KOUSSERI', 'KOUSSERI'),
        ('KOUSSERI', 'KOUSSERI'),
        ('AIRD', 'AIRD'),
    )

    designation = models.CharField(max_length=100,null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    quantity = models.PositiveIntegerField(null=True)
    unite = models.CharField(max_length=10,null=True)
    emplacement = models.CharField(max_length=25, choices=EMPLACEMENT)

    def __str__(self):
        return self.designation

class hightech(models.Model):
    MARQUE = (
        ('TECHNO SPARK 8','TECHNO SPARK 8'),
        ('TECHNO CAMON 16','TECHNO CAMON 16'),
        ('CHARGEUR TECNO SPARK','CHARGEUR TECNO SPARK'),
        ('TABLETTE TECHNO P 701','TABLETTE TECHNO P 701'),
        ('TABLETTE TECHNO P 703','TABLETTE TECHNO P 703'),
        ('TABLETTE TECHNO PP7E','TABLETTE TECHNO PP7E'),
    )

    EMPLACEMENT = (
        ('SALLE SPORT', 'SALLE SPORT'),
        ('SALLE SERVEUR', 'SALLE SERVEUR'),
        ('CENTRE TRANSIT', 'CENTRE TRANSIT'),
        ('CARTON DIMA', 'CARTON DIMA'),
        ('MINAWAO', 'MINAWAO'),
        ('KOUSSERI', 'KOUSSERI'),
        ('KOUSSERI', 'KOUSSERI'),
        ('AIRD', 'AIRD'),
    )
    marque = models.CharField(max_length=100, choices=MARQUE)
    quantity = models.PositiveIntegerField(null=True)
    num_serie = models.CharField(max_length=35,null=True)
    imei = models.CharField(max_length=35,null=True)
    emplacement = models.CharField(max_length=25, choices=EMPLACEMENT)

    def __str__(self):
        return self.marque

class laptop(models.Model):
    BRAND = (
        ('T14S GEN 1 (Lenovo)', 'T14S GEN 1 (Lenovo)'),
        ('T450S (Lenovo)', 'T450S (Lenovo)'),
        ('81HN (Lenovo)', '81HN (Lenovo)'),
    )
    EMPLACEMENT = (
        ('SALLE SPORT', 'SALLE SPORT'),
        ('SALLE SERVEUR', 'SALLE SERVEUR'),
        ('CENTRE TRANSIT', 'CENTRE TRANSIT'),
        ('MINAWAO', 'MINAWAO'),
        ('KOUSSERI', 'KOUSSERI'),
        ('KOUSSERI', 'KOUSSERI'),
        ('AIRD', 'AIRD'),
    )
    brand = models.CharField(max_length=100, choices=BRAND)
    quantity = models.PositiveIntegerField(null=True)
    num_serie = models.CharField(max_length=35, null=True)
    imei = models.CharField(max_length=35, null=True)
    emplacement = models.CharField(max_length=25, choices=EMPLACEMENT)

    def __str__(self):
        return self.brand

class SortieMat(models.Model):
    designation = models.CharField(max_length=100,null=True)
    quantity = models.PositiveIntegerField(null=True)
    decharge = models.CharField(max_length=100)
    utilisation=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.designation
