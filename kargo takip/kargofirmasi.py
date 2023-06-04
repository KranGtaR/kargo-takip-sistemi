from kargo import Kargo

# KargoFirmasi sınıfı
class KargoFirmasi(Kargo):
    def __init__(self, numara, teslimat_durumu, teslim_edilebilme_durumu, gonderi_tarihi, alici_ad, alici_adres, gonderici, firma_adi):
        super().__init__(numara, teslimat_durumu, teslim_edilebilme_durumu, gonderi_tarihi, alici_ad, alici_adres, gonderici)
        self.firma_adi = firma_adi
    
    def teslimat_sorgula(self):
        if self.teslimat_durumu == "Teslim Edildi":
            return "Kargo teslim edildi."
        else:
            return "Kargo hala teslim edilmedi."
    
    def odeme_yap(self, odeme_tutari):
        # Ödeme işlemleri burada yapılır.
        self.teslimat_durumu = "Ödeme Yapıldı"
    
    def bilgileri_guncelle(self, alici_ad, alici_adres):
        self.alici_ad = alici_ad
        self.alici_adres = alici_adres
    
    def getInfo(self):
        return super().getInfo() + f"\nFirma Adı: {self.firma_adi}"
