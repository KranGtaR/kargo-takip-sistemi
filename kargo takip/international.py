from kargo import Kargo

# InternationalKargo sınıfı
class InternationalKargo(Kargo):
    def __init__(self, numara, teslimat_durumu, teslim_edilebilme_durumu, gonderi_tarihi, alici_ad, alici_adres, gonderici, hedef_ulke):
        super().__init__(numara, teslimat_durumu, teslim_edilebilme_durumu, gonderi_tarihi, alici_ad, alici_adres, gonderici)
        self.hedef_ulke = hedef_ulke
    
    def yurtdisi_gonderi_bilgisi(self):
        pass
    
    def getInfo(self):
        return super().getInfo() + f"\nHedef Ülke: {self.hedef_ulke}"
