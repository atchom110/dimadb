from django.db import models
from django.utils import timezone


# Create your models here.
class Category(models.Model):
    CATEGORY = (
        ('ENCRE', 'ENCRE'),
        ('ENCRE FARGO', 'ENCRE FARGO'),
        ('TONER', 'TONER'),
        ('KIT BIMS', 'KIT BIMS'),
        ('IMPRIMANTE', 'IMPRIMANTE'),
        ('SECURITE', 'SECURITE'),
        ('MAT RESEAU', 'MAT RESEAU'),
        ('MAT BUREAU', 'MAT BUREAU'),
        ('ENREGISTREMENT', 'ENREGISTREMENT'),
        ('ORDINATEUR', 'ORDINATEUR'),
        ('TELEPHONE', 'TELEPHONE'),
    )
    name = models.CharField(max_length=25, choices=CATEGORY)

    def __str__(self):
        return self.name

class Product(models.Model):
    EMPLACEMENT = (
        ('SALLE SPORT','SALLE SPORT'),
        ('SALLE SERVEUR','SALLE SERVEUR'),
        ('CENTRE TRANSIT', 'CENTRE TRANSIT'),
        ('BUREAU MINAWAO', 'BUREAU MINAWAO'),
        ('BUREAU KOUSSERI', 'BUREAU KOUSSERI'),
        ('BUREAU AIRD', 'BUREAU AIRD'),
    )
    ARRIVAGE = (
        ('OUI', 'OUI'),
        ('NON', 'NON'),
    )

    designation = models.CharField(max_length=100,null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    quantity = models.PositiveIntegerField(null=True)
    qte_sortie = models.PositiveIntegerField(null=True)
    unite = models.CharField(max_length=10,null=True)
    emplacement = models.CharField(max_length=25, choices=EMPLACEMENT)
    arrivage = models.CharField(max_length=25, choices=ARRIVAGE,null=True)
    date_entree = models.DateField(null=True, blank=True)

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
        ('SAC KAKI', 'SAC KAKI'),
        ('COFFRE BABA', 'COFFRE BABA'),
        ('BUREAU MINAWAO', 'BUREAU MINAWAO'),
        ('BUREAU KOUSSERI', 'BUREAU KOUSSERI'),
        ('BUREAU AIRD', 'BUREAU AIRD'),
        ('CARTON NEUF', 'CARTON NEUF'),
    )
    ARRIVAGE= (
        ('OUI', 'OUI'),
        ('NON', 'NON'),
    )
    SORTIE = (
        ('OUI', 'OUI'),
        ('NON', 'NON'),
    )
    marque = models.CharField(max_length=100, choices=MARQUE)
    quantity = models.PositiveIntegerField(null=True)
    num_serie = models.CharField(max_length=35,null=True)
    user = models.CharField(max_length=35, null=True)
    imei = models.CharField(max_length=35,null=True)
    emplacement = models.CharField(max_length=25, choices=EMPLACEMENT)
    arrivage = models.CharField(max_length=25, choices=ARRIVAGE,null=True)
    date_entree = models.DateField(null=True, blank=True)
    sortie = models.CharField(max_length=25, choices=SORTIE, null=True)

    def __str__(self):
        return self.marque

class laptop(models.Model):
    BRAND = (
        ('T14S GEN 1 (Lenovo)', 'T14S GEN 1 (Lenovo)'),
        ('T450S (Lenovo)', 'T450S (Lenovo)'),
        ('81HN (Lenovo)', '81HN (Lenovo)'),
        ('T14S GEN 3 (Lenovo)', 'T14S GEN 3 (Lenovo)'),
        ('P16 GEN 1 (Lenovo)', 'P16 GEN 1 (Lenovo)'),
        ('X1 EXTREME G 5 (Lenovo)', 'X1 EXTREME G 5 (Lenovo)'),
    )
    EMPLACEMENT = (
        ('SALLE SPORT', 'SALLE SPORT'),
        ('SALLE SERVEUR', 'SALLE SERVEUR'),
        ('CENTRE TRANSIT', 'CENTRE TRANSIT'),
        ('STAFF', 'STAFF'),
        ('AGENT ENREG', 'AGENT ENREG'),
        ('BUREAU MINAWAO', 'BUREAU MINAWAO'),
        ('BUREAU KOUSSERI', 'BUREAU KOUSSERI'),
        ('BUREAU AIRD', 'BUREAU AIRD'),
    )
    ARRIVAGE = (
        ('NEUF', 'NEUF'),
        ('OUI', 'OUI'),
        ('NON', 'NON'),

    )
    SORTIE = (
        ('OUI', 'OUI'),
        ('NON', 'NON'),
    )

    brand = models.CharField(max_length=100, choices=BRAND)
    quantity = models.PositiveIntegerField(null=True)
    user = models.CharField(max_length=35, null=True)
    num_serie = models.CharField(max_length=35, null=True)
    imei = models.CharField(max_length=35, null=True)
    emplacement = models.CharField(max_length=25, choices=EMPLACEMENT)
    arrivage = models.CharField(max_length=25, choices=ARRIVAGE,null=True)
    date_entree = models.DateField(null=True, blank=True)
    sortie = models.CharField(max_length=25, choices=SORTIE, null=True)

    def __str__(self):
        return self.brand


class sortieMat1(models.Model):
    DUREE = (
        ('TEMPORAIRE', 'TEMPORAIRE'),
        ('DEFINITIF', 'DEFINITIF'),
    )
    RETOUR = (
        ('OUI', 'OUI'),
        ('NON', 'NON'),
    )
    designation = models.CharField(max_length=50,null=True)
    quantity = models.PositiveIntegerField(null=True)
    decharge = models.CharField(max_length=50, null=True)
    info = models.CharField(max_length=100, null=True)
    duree = models.CharField(max_length=25, choices=DUREE, null=True)
    date_sortie = models.DateField(auto_now_add=False, auto_now=False, null=True)
    retour = models.CharField(max_length=25, choices=RETOUR, null=True)
   # date_retour = models.DateField(auto_now_add=False, auto_now=False, null=True)
    date_retour = models.DateField(null=True, blank=True)
    def __str__(self):
        return self.designation
