from django.db import models

class ReseptiAines(models.Model):
    aines = models.CharField(max_length=100)
    maara = models.DecimalField(max_digits=10, decimal_places=2)
    yksikko = models.CharField(max_length=10)
    def __str__(self):
        return f"{self.aines} {self.maara} {self.yksikko}"

class Vaihe(models.Model):
    kuvaus = models.TextField()
    aika_minuuttia = models.IntegerField(default=0)  # Aika minuutteina

    class Meta:
        ordering = ['id']  # Järjestetään vaiheiden mukaan

    def __str__(self):
        return f"Vaihe {self.id} - {self.kuvaus}"

class Resepti(models.Model):
    nimi = models.CharField(max_length=100)
    kuvaus = models.TextField(blank=True, null=True)
    aika_minuuttia = models.IntegerField(default=0)  # Aika minuutteina
    ainekset = models.ManyToManyField(ReseptiAines, related_name='reseptit')
    vaiheet = models.ManyToManyField(Vaihe, related_name='reseptit')
    def __str__(self):
        return self.nimi
