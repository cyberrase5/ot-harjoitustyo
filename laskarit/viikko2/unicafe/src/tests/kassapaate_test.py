import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):

    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_alku_kassa(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_alku_edulliset(self):
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_alku_maukkaat(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)



    def test_edullisesti_kateisella_maara(self):
        self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_edullisesti_kateisella_kassa(self):
        saldo = self.kassapaate.kassassa_rahaa + 240
        self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, saldo)


    def test_edullisesti_kortilla_maara(self):
        kortti = Maksukortti(1000)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_edullisesti_kortilla_bool(self):
        kortti = Maksukortti(1000)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(kortti), True)


    def test_ei_rahaa_edullisesti_kateisella_maara(self):
        self.kassapaate.syo_edullisesti_kateisella(5)
        self.assertEqual(self.kassapaate.edulliset, 0)

    

    def test_ei_rahaa_edullisesti_kortilla_maara(self):
        kortti = Maksukortti(10)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_ei_rahaa_edullisesti_kortilla_bool(self):
        kortti = Maksukortti(10)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(kortti), False)


    def test_lataa_rahaa_positiivinen(self):
        kortti = Maksukortti(1000)
        self.kassapaate.lataa_rahaa_kortille(kortti, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100100)

    def test_lataa_rahaa_negatiivinen(self):
        kortti = Maksukortti(1000)
        self.kassapaate.lataa_rahaa_kortille(kortti, -100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)


    def test_maukkaasti_kateisella_maara(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_maukkaasti_kateisella_kassa(self):
        saldo = self.kassapaate.kassassa_rahaa + 400
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, saldo)


    def test_maukkaasti_kortilla_maara(self):
        kortti = Maksukortti(1000)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_maukkaasti_kortilla_bool(self):
        kortti = Maksukortti(1000)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(kortti), True)


    def test_ei_rahaa_maukkaasti_kateisella_maara(self):
        self.kassapaate.syo_maukkaasti_kateisella(5)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    

    def test_ei_rahaa_maukkaasti_kortilla_maara(self):
        kortti = Maksukortti(10)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_ei_rahaa_maukkaasti_kortilla_bool(self):
        kortti = Maksukortti(10)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(kortti), False)
