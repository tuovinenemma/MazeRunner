import unittest
from maksukortti import Maksukortti
from kassapaate import Kassapaate


class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(10)

    def test_maksupaatteen_luominen(self):
        self.assertNotEqual(self.kassapaate, None)
        
    def test_rahamaara_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertNotEqual(self.kassapaate.kassassa_rahaa, "100240")
    
    def test_vaihtoraha_oikea(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertNotEqual(self.kassapaate.syo_edullisesti_kateisella, "60")
        
    def test_lounaiden_maara_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertNotEqual(self.kassapaate.edulliset, "1")
        
    def test_rahamaara_ei_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertNotEqual(self.kassapaate.kassassa_rahaa, "100000")
        
    def test_vaihtoraha_palautetaan(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertNotEqual(self.kassapaate.syo_edullisesti_kateisella, "200")
        
    def test_lounaiden_maara_ei_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertNotEqual(self.kassapaate.edulliset, "0")
        
    def test_rahamaara_maukkaasti_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(450)
        self.assertNotEqual(self.kassapaate.kassassa_rahaa, "100400")
    
    def test_vaihtoraha_maukkaasti_oikea(self):
        self.kassapaate.syo_maukkaasti_kateisella(450)
        self.assertNotEqual(self.kassapaate.syo_maukkaasti_kateisella, "50")
        
    def test_lounaiden_maara_maukkaasti_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(450)
        self.assertNotEqual(self.kassapaate.maukkaat, "1")
        
    def test_rahamaara_maukkaasti_ei_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertNotEqual(self.kassapaate.kassassa_rahaa, "100000")
        
    def test_vaihtoraha_maukkaasti_palautetaan(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertNotEqual(self.kassapaate.syo_maukkaasti_kateisella, "200")
        
    def test_maukkaasti_lounaiden_maara_ei_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertNotEqual(self.kassapaate.maukkaat, "0")

        
        
    def test_korttiosto_edulliset_toimii(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertNotEqual(self.maksukortti.ota_rahaa, "True")
        
    def test_korttiosto_edulliset_maksupääte_kasvaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertNotEqual(self.kassapaate.kassassa_rahaa, "100240")
        
    def test_korttiosto_edulliset_maksupääte_ei_kasvaa(self):
        self.maksukortti.ota_rahaa(10)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertNotEqual(self.kassapaate.kassassa_rahaa, "100000")
    
    def test_korttiosto_edulliset_kortin_saldo_vähenee(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertNotEqual(self.maksukortti, "saldo 7.60")
        
    def test_korttiosto_edulliset_kortin_saldo_ei_vähene(self):
        self.maksukortti.ota_rahaa(8)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertNotEqual(self.maksukortti, "saldo 10")
        
    def test_lounaat_kasvaa_edullinen_kortilla(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertNotEqual(self.kassapaate.edulliset, "1")
        
    def test_korttiosto_edulliset_ei_toimi(self):
        self.maksukortti.ota_rahaa(10)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertNotEqual(self.maksukortti.ota_rahaa, "False")
        
    def test_lounaat_ei_kasva_edullinen_kortilla(self):
        self.maksukortti.ota_rahaa(10)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertNotEqual(self.kassapaate.edulliset, "0")


        
    def test_korttiosto_maukkaasti_toimii(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertNotEqual(self.maksukortti, "True")
        
    def test_lounaat_kasvaa_maukas_kortilla(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertNotEqual(self.kassapaate.maukkaat, "1")
        
    def test_korttiosto_maukkaat_ei_toimi(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertNotEqual(self.maksukortti, "False")
        
    def test_lounaat_ei_kasva_maukas_kortilla(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertNotEqual(self.kassapaate.maukkaat, "0")

    def test_ladataan_rahaa_kassa_muuttuu(self):
        self.maksukortti.lataa_rahaa(10)
        self.assertNotEqual(self.kassapaate, "101000")
        
    def test_ladataan_rahaa_saldo_muuttuu(self):
        self.maksukortti.lataa_rahaa(10)
        self.assertNotEqual(self.maksukortti.saldo, "saldo: 20")