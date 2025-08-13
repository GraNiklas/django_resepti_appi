from django.test import TestCase
from app.models import Resepti, Vaihe, ReseptiAines

# Create your tests here.
class ReseptiModelTest(TestCase):
    def setUp(self):
        # Set up any necessary data for the tests
        pass
    def test_resepti_creation(self):
        # Test that a Resepti object can be created successfully
        resepti = Resepti.objects.create(nimi="Testiresepti", aika_minuuttia=30, kuvaus="Testikuvaus")
        self.assertIsInstance(resepti, Resepti)
        self.assertEqual(resepti.nimi, "Testiresepti")
        self.assertEqual(resepti.kuvaus, "Testikuvaus")
        self.assertEqual(resepti.aika_minuuttia, 30)
    
    def test_vaihe_creation(self):
        # Test that a Vaihe object can be created successfully
        vaihe = Vaihe.objects.create(kuvaus="Testivaihe", aika_minuuttia=10)
        self.assertIsInstance(vaihe, Vaihe)
        self.assertEqual(vaihe.kuvaus, "Testivaihe")
        self.assertEqual(vaihe.aika_minuuttia, 10)

    def test_resepti_aines_creation(self):
        resepti_aines = ReseptiAines.objects.create(aines = "Testaines", maara=100, yksikko="g")
        self.assertEqual(resepti_aines.aines, "Testaines")
        self.assertEqual(resepti_aines.maara, 100)
        self.assertEqual(resepti_aines.yksikko, "g")

class ReseptiTests(TestCase):
    def test_uusi_resepti(self):
        response = self.client.get('/uusi-resepti/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'resepti.html')
    