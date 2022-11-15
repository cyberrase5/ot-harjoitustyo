import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)


    def test_alkuasaldo_oikein(self):
        self.assertEqual(self.maksukortti.saldo, 1000)


    def test_lisaa_positiivinen(self):
        self.maksukortti.lataa_rahaa(100)
        self.assertEqual(self.maksukortti.saldo, 1100)

    def test_lisaa_negatiivinen(self):
        self.maksukortti.lataa_rahaa(-100)
        self.assertEqual(self.maksukortti.saldo, 900)


    def test_ota_riittavasti(self):
        self.maksukortti.ota_rahaa(500)
        self.assertEqual(self.maksukortti.saldo, 500)

    def test_ota_riittavasti_bool(self):
        self.assertEqual(self.maksukortti.ota_rahaa(500), True)

    def test_ota_liikaa(self):
        self.maksukortti.ota_rahaa(1500)
        self.assertEqual(self.maksukortti.saldo, 1000)

    def test_ota_liikaa_bool(self):
        self.assertEqual(self.maksukortti.ota_rahaa(1500), False)

    def test_ota_negatiivinen(self):
        self.maksukortti.ota_rahaa(-500)
        self.assertEqual(self.maksukortti.saldo, 1500)

    def test_str(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")